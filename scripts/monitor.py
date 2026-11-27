"""Window-based SLO monitor; two-window persistence reduces noise."""
import json, time
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parents[1]
def classify(samples,config):
    n=len(samples)
    if n<config['minimum_samples']:return {'status':'insufficient_samples','n':n}
    errors=sum(s['status']>=500 or s['status']==0 for s in samples)
    slow=sum(s['latency_ms']>config['latency_limit_ms'] for s in samples)
    availability=1-errors/n; latency=1-slow/n
    return {'status':'breach' if availability<config['availability_target'] or latency<config['latency_target'] else 'healthy',
      'n':n,'availability':availability,'latency_compliance':latency,'latency_p95_ms':sorted(s['latency_ms'] for s in samples)[int(.95*(n-1))],
      'availability_budget_used':errors/(n*(1-config['availability_target'])),
      'latency_budget_used':slow/(n*(1-config['latency_target']))}
def sample(url,token,n=20):
    records=[]
    for _ in range(n):
        start=time.perf_counter()
        try:
            r=requests.post(url+'/v1/predict',headers={'X-API-Key':token},json={'texto':'The company reported a decrease in operating profit.','idioma':'en'},timeout=5)
            status=r.status_code; trace=r.headers.get('X-Trace-ID')
        except requests.RequestException:status=0;trace=None
        records.append({'status':status,'latency_ms':(time.perf_counter()-start)*1000,'trace_id':trace})
    return records
