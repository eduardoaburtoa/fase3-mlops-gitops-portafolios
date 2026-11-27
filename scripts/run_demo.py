"""Real local container experiments; deliberately injected faults are labelled."""
import argparse,json,os,sys,time,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from scripts.reconcile import reconcile,docker,DOCKER
from scripts.monitor import sample,classify
p=argparse.ArgumentParser();p.add_argument('--image',required=True);args=p.parse_args()
cfg=json.loads((ROOT/'deploy/staging.json').read_text());slo=json.loads((ROOT/'config/slo.json').read_text())
url=f"http://127.0.0.1:{cfg['port']}";token=os.environ['API_TOKEN']
results={'scope':'Executed Docker laboratory, not production','started_unix':time.time(),'windows':[]}
results['initial']=reconcile(args.image)
results['idempotent']=reconcile(args.image)
assert results['idempotent']['action']=='noop'
def window(label):
    rows=sample(url,token); summary=classify(rows,slo)
    assert all(r['status']==200 for r in rows),rows
    results['windows'].append({'label':label,'summary':summary,'samples':rows});return summary
assert window('baseline')['status']=='healthy'
docker('stop',cfg['container']);results['drift_recovery']=reconcile(args.image)
results['incident_readiness']=reconcile(args.image,unready=True)
assert results['incident_readiness']['recovered']
results['latency_deploy']=reconcile(args.image,delay=400)
breaches=[window('injected_latency_1'),window('injected_latency_2')]
assert all(w['status']=='breach' for w in breaches)
results['alert']={'severity':'P2','reason':'Two consecutive latency SLO breaches','automatic_action':'rollback','simulation':True}
results['latency_rollback']=reconcile(args.image,rollback=True)
assert window('recovered')['status']=='healthy'
results['finished_unix']=time.time();results['all_assertions_passed']=True
(ROOT/'evidencias/despliegue.json').write_text(json.dumps(results,indent=2))
(ROOT/'evidencias/auditoria.jsonl').write_text((ROOT/'runtime/audit.jsonl').read_text())
logs=subprocess.run([DOCKER,'logs',cfg['container']],capture_output=True,text=True,check=True)
lines=[]
for line in (logs.stdout+'\n'+logs.stderr).splitlines():
    start=line.find('{')
    if start>=0:
        try: lines.append(json.dumps(json.loads(line[start:])))
        except json.JSONDecodeError: pass
assert lines, 'Missing structured request logs'
(ROOT/'evidencias/container_logs.jsonl').write_text('\n'.join(lines)+'\n')
print(json.dumps({k:v for k,v in results.items() if k!='windows'},indent=2))
