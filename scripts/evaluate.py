"""Re-evaluation of a frozen model; no test-set tuning."""
import json, sys
from pathlib import Path
import joblib, numpy as np, pandas as pd
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,confusion_matrix
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from scripts.check_data import validate

def evaluate():
    validate()
    model=joblib.load(ROOT/'modelos/modelo_SVM_calibrada.joblib')
    data=pd.read_csv(ROOT/'datos/predicciones_test.csv')
    p=model.predict_proba(data.texto)[:,1]
    np.testing.assert_allclose(p,data.SVM_calibrada,rtol=1e-7,atol=1e-9)
    pred=p>=.2; y=data.y
    metrics={'accuracy':accuracy_score(y,pred),'precision':precision_score(y,pred),'recall':recall_score(y,pred),'f1':f1_score(y,pred),'roc_auc':roc_auc_score(y,p)}
    import mlflow, mlflow.sklearn
    mlflow.set_tracking_uri((ROOT/'runtime/mlruns').as_uri())
    mlflow.set_experiment('FaseIII-validacion-congelada')
    with mlflow.start_run() as run:
        mlflow.log_params({'threshold':.2,'scope':'academic','test_used_for_tuning':False,'model_sha256':json.loads((ROOT/'modelos/manifest.json').read_text())['sha256']})
        mlflow.log_metrics(metrics)
        info=mlflow.sklearn.log_model(model,'model',input_example=data.texto.to_numpy()[:2],signature=mlflow.models.infer_signature(data.texto.to_numpy()[:2],model.predict(data.texto.iloc[:2])))
        restored=mlflow.sklearn.load_model(info.model_uri)
        np.testing.assert_array_equal(p,restored.predict_proba(data.texto)[:,1])
        mlflow.log_artifact(str(ROOT/'config/data_manifest.json'))
        result={'metrics':metrics,'confusion_matrix':confusion_matrix(y,pred).tolist(),'threshold':.2,'n':len(y),'run_id':run.info.run_id,'reload_identical':True,'scope':'Frozen historical test; not Mexican fund returns validation'}
        mlflow.log_dict(result,'evaluation.json')
    (ROOT/'evidencias/evaluacion.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
    return result
if __name__=='__main__': evaluate()
