"""Declarative, local Docker deployment with health gate and rollback."""
import argparse, hashlib, json, os, subprocess, time
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parents[1]
STATE=ROOT/'runtime/deployment.json'
DOCKER=os.environ.get('DOCKER','docker')
def docker(*args,check=True):
    return subprocess.run([DOCKER,*args],capture_output=True,text=True,check=check).stdout.strip()
def audit(event,**fields):
    path=ROOT/'runtime/audit.jsonl'; path.parent.mkdir(exist_ok=True)
    with path.open('a') as f: f.write(json.dumps({'time_unix':time.time(),'event':event,**fields})+'\n')
def healthy(cfg):
    try:
        r=requests.get(f"http://127.0.0.1:{cfg['port']}/health",timeout=2)
        return r.status_code==200
    except requests.RequestException: return False

def start(cfg,image,token,delay=0,unready=False):
    docker('rm','-f',cfg['container'],check=False)
    # Pass secret through process environment, never as a command-line value.
    os.environ['API_TOKEN']=token
    docker('run','-d','--name',cfg['container'],'--cpus',str(cfg['cpu_limit']),'--memory',cfg['memory_limit'],
           '-p',f"127.0.0.1:{cfg['port']}:8000",'-e','API_TOKEN','-e',f'DEMO_DELAY_MS={delay}',
           '-e',f'FAIL_READINESS={int(unready)}',image)
    timeout=8 if unready else cfg['readiness_timeout_seconds']
    end=time.monotonic()+timeout
    while time.monotonic()<end:
        if healthy(cfg):
            m=requests.get(f"http://127.0.0.1:{cfg['port']}/v1/model",headers={'X-API-Key':token},timeout=3)
            if m.status_code==200 and cfg['model_sha256'] in m.text:return True
        time.sleep(.5)
    return False

def reconcile(image,delay=0,unready=False,rollback=False):
    cfg=json.loads((ROOT/'deploy/staging.json').read_text())
    if cfg['production_authorized'] or cfg['environment']!='academic-staging':raise ValueError('Academic environment only')
    token=os.environ.get('API_TOKEN','')
    if len(token)<16: raise ValueError('Set API_TOKEN with at least 16 characters')
    STATE.parent.mkdir(exist_ok=True)
    old=json.loads(STATE.read_text()) if STATE.exists() else {}
    digest=hashlib.sha256((ROOT/'deploy/staging.json').read_bytes()).hexdigest()
    image_id=docker('image','inspect',image,'--format','{{.Id}}')
    candidate={'image':image_id,'delay':delay,'config_sha':digest}
    if rollback:
        candidate=old.get('previous')
        if not candidate:raise ValueError('No previous healthy deployment')
        unready=False
    if old.get('active')==candidate and healthy(cfg) and not unready:
        audit('reconcile_noop',image=image_id);return {'action':'noop','active':candidate}
    audit('deploy_started',candidate=candidate,simulated_failure=unready)
    ok=start(cfg,candidate['image'],token,candidate['delay'],unready)
    if not ok:
        previous=old.get('active')
        recovered=bool(previous and start(cfg,previous['image'],token,previous['delay']))
        audit('readiness_failed',rollback_recovered=recovered)
        if not recovered:raise RuntimeError('Deployment failed; no healthy rollback available')
        return {'action':'rollback_after_failed_readiness','recovered':True,'active':previous}
    result={'active':candidate,'previous':old.get('active'),'action':'rollback' if rollback else 'deploy'}
    STATE.write_text(json.dumps(result,indent=2));audit('deploy_healthy',**result)
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--image',required=True);p.add_argument('--delay',type=int,default=0);p.add_argument('--unready',action='store_true');p.add_argument('--rollback',action='store_true');a=p.parse_args()
    print(json.dumps(reconcile(a.image,a.delay,a.unready,a.rollback),indent=2))
