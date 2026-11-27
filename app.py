"""Evidence dashboard: historical measurements are explicitly labelled."""
from pathlib import Path
import json
import pandas as pd
import streamlit as st
ROOT=Path(__file__).parent
st.set_page_config(page_title='Vértice AI · Fase III',page_icon='🔷',layout='wide')
st.image(str(ROOT/'documentos/vertice_logo.png'),width=150)
st.title('Fase III · Resultados verificables')
st.caption('Eduardo Aburto Angulo · Prototipo académico · Revisión humana de portafolios')
st.info('Este tablero muestra evidencias guardadas de laboratorio. No ejecuta operaciones ni estima rendimientos futuros.')
def read(name):
    p=ROOT/'evidencias'/name
    return json.loads(p.read_text()) if p.exists() else None
page=st.sidebar.radio('Guía de contenido',['Resultados','Pipeline y operación','Incidentes','Contexto de negocio','Documentación'])
if page=='Resultados':
    d=read('evaluacion.json')
    if d:
        cols=st.columns(5)
        for col,(k,v) in zip(cols,d['metrics'].items()):col.metric(k,f'{v:.3f}')
        st.subheader('Matriz de confusión · test histórico congelado')
        st.dataframe(pd.DataFrame(d['confusion_matrix'],index=['Real no negativa','Real negativa'],columns=['Predicha no negativa','Predicha negativa']))
        st.write('452 noticias financieras en inglés; clase positiva = noticia negativa. No valida idoneidad de fondos mexicanos.')
        st.json({'MLflow_run_id':d['run_id'],'recarga_idéntica':d['reload_identical'],'umbral_congelado':d['threshold']})
    else:st.warning('Ejecuta scripts/evaluate.py para generar evidencia.')
elif page in ['Pipeline y operación','Incidentes']:
    d=read('despliegue.json')
    if d:
        rows=[{'ventana':w['label'],**w['summary']} for w in d['windows']]
        st.dataframe(pd.DataFrame(rows),hide_index=True)
        st.bar_chart(pd.DataFrame(rows).set_index('ventana')['latency_p95_ms'])
        st.json(d['alert']);st.json({k:v for k,v in d.items() if k!='windows'})
    else:st.warning('Evidencia de despliegue pendiente de ejecución.')
elif page=='Contexto de negocio':
    st.write('Como banquero Sr., priorizo que una revisión aporte valor neto al cliente y respete su perfil. Una noticia negativa sólo motiva revisión; no ordena una migración.')
    df=pd.read_csv(ROOT/'contexto/clientes_simulados.csv');st.dataframe(df,hide_index=True)
    st.caption('150 personajes ficticios para fines didácticos; posiciones entre 5 y 20 millones de pesos. Corretaje 1 % por compra y 1 % por venta: supuesto académico, no tarifa verificada de BBVA.')
else:
    base='https://github.com/eduardoaburtoa/fase3-mlops-gitops-portafolios'
    st.link_button('Abrir portada y entregables',base)
    st.write('Pipeline, operación, portfolio, entrevista y evidencias estarán enlazados desde la portada.')
