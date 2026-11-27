"""Métricas y trazas locales sin textos, identidades ni credenciales."""
import collections,json,logging,threading,time,uuid
LOCK=threading.Lock()
COUNTS=collections.Counter()
LATENCIES=collections.deque(maxlen=2000)
LOGGER=logging.getLogger('uvicorn.error')

def record(method,path,status,seconds,model_sha,trace_id):
    with LOCK:
        COUNTS['requests']+=1
        COUNTS['errors']+=int(status>=500)
        LATENCIES.append(seconds*1000)
    LOGGER.info(json.dumps(dict(event='http_request',method=method,route=path,status=status,latency_ms=round(seconds*1000,3),model_sha256=model_sha,trace_id=trace_id),ensure_ascii=False))

def snapshot():
    with LOCK:return {'requests':COUNTS['requests'],'server_errors':COUNTS['errors'],'latency_ms':list(LATENCIES),'retention':'2000 mediciones en memoria; reinicio borra contadores'}
