import os
os.environ['API_TOKEN']='academic-test-token-only'
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from scripts.check_data import validate
from scripts.monitor import classify
HEAD={'X-API-Key':os.environ['API_TOKEN']}
@pytest.fixture
def client():
    with TestClient(app) as c:yield c

def test_data():assert validate()['test_rows']==452

def test_api_auth_and_trace(client):
    assert client.get('/v1/model').status_code==401
    r=client.post('/v1/predict',headers=HEAD,json={'texto':'The company reported lower operating profit.'})
    assert r.status_code==200 and len(r.headers['X-Trace-ID'])==32
    assert 0<=r.json()['probabilidad_negativa']<=1
    assert client.get('/v1/metrics',headers=HEAD).json()['requests']>=1

@pytest.mark.parametrize('body',[{'texto':'12'},{'texto':'hola','idioma':'es'},{'texto':'valid text','unexpected':True},{'texto':'x'*4001}])
def test_invalid_inputs(client,body):assert client.post('/v1/predict',headers=HEAD,json=body).status_code==422

def test_scenario(client):
    c=client.get('/v1/clients',headers=HEAD).json()['clientes'][0]
    payload={'cliente_id':c['cliente_id'],'proporcion':.1,'mejora_anual_pp':1,'meses':12,'gastos_adicionales_anuales_pp':0,'perfil_destino':c['perfil_riesgo']}
    r=client.post('/v1/scenario',headers=HEAD,json=payload).json()
    assert r['beneficio_incremental_supuesto_mxn']<0 and not r['elegible_para_revision']
    payload['proporcion']=float('nan')
    # JSON disallows NaN; verify schema directly instead.
    from backend.main import Scenario
    from pydantic import ValidationError
    with pytest.raises(ValidationError):Scenario(**payload)

def test_slo():
    cfg={'minimum_samples':20,'latency_limit_ms':250,'availability_target':.99,'latency_target':.99}
    assert classify([],cfg)['status']=='insufficient_samples'
    assert classify([{'status':200,'latency_ms':400}]*20,cfg)['status']=='breach'
    assert classify([{'status':200,'latency_ms':10}]*20,cfg)['status']=='healthy'
    assert classify([{'status':500,'latency_ms':10}]*20,cfg)['availability']==0

def test_readiness_failure(client,monkeypatch):
    monkeypatch.setenv('FAIL_READINESS','1')
    assert client.get('/health').status_code==503
