"""Fail-closed validation of frozen academic artifacts."""
import hashlib, json
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def validate():
    manifest=json.loads((ROOT/'config/data_manifest.json').read_text())
    for name, expected in manifest.items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=expected:
            raise ValueError(f'Hash mismatch: {name}')
    df=pd.read_csv(ROOT/'datos/predicciones_test.csv')
    assert df.id.is_unique and not df[['texto','y']].isna().any().any()
    assert set(df.y)=={0,1}
    clients=pd.read_csv(ROOT/'contexto/clientes_simulados.csv')
    assert len(clients)==150 and clients.cliente_id.is_unique
    assert clients.posicion_mxn.between(5_000_000,20_000_000).all()
    assert set(clients.perfil_riesgo)<= {'Conservador','Moderado','Agresivo'}
    assert df.y.eq(df.etiqueta.eq('negative').astype(int)).all()
    return {'status':'passed','hashes':manifest,'test_rows':len(df),'simulated_clients':len(clients)}
if __name__=='__main__':
    result=validate(); print(json.dumps(result,indent=2))
    (ROOT/'evidencias/validacion_datos.json').write_text(json.dumps(result,indent=2))
