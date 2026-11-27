# Pipeline automatizado de inteligencia artificial

Eduardo Aburto Angulo · Fase III

## Decisión y alcance

Construí un flujo reproducible que valida el modelo congelado, registra la evaluación en MLflow y despliega una API mediante Docker. Mi decisión es demostrar el ciclo operativo en un entorno académico aislado antes de plantear una incorporación bancaria. La configuración mantiene production_authorized=false. El servicio no decide operaciones financieras.
La continuidad conserva el modelo de Actividad 6 y la API de Fase II. Actividades 8 y 9 aportan observabilidad, límites y gobierno. Las referencias exactas de código están en evidencias/procedencia.json. No volví a elegir el umbral con el test.

## Integración y versionamiento

Cada push a main ejecuta dos trabajos: validate y deploy-staging. Las solicitudes de cambio ejecutan validación sin despliegue. validate instala dependencias fijadas, comprueba contratos de datos y API, reevalúa el modelo y exporta los artefactos MLflow. deploy-staging depende del éxito de validate, construye una imagen etiquetada con el SHA del commit y ejecuta el reconciliador.
Git versiona código, configuración y manifiestos. SHA-256 fija los bytes del modelo, test y clientes ficticios. El modelo se verifica antes de deserializarlo. MLflow conserva parámetros, métricas, modelo y evaluación; su recarga se contrasta con predicciones idénticas. El paquete joblib sólo debe cargarse si procede de este origen confiable; el hash aporta integridad, no una firma de autoría.

## Despliegue y reconciliación

deploy/staging.json define nombre, puerto, límites y hash esperado. El reconciliador resuelve la imagen a un identificador inmutable, inicia el contenedor y verifica /health y /v1/model con autenticación. Una segunda reconciliación sin cambios no recrea el servicio. Si el contenedor desaparece, restaura el estado deseado.
El laboratorio usa un contenedor único y por tanto puede interrumpir brevemente el servicio durante el reemplazo. No acredita despliegue sin interrupciones ni alta disponibilidad. Si falla la verificación de salud, restaura la configuración anterior. El experimento de latencia revierte la configuración de la misma imagen; no simula una nueva versión entrenada. El ejecutor de GitHub es temporal y no constituye una URL pública permanente.

## Pruebas y evidencia

La ejecución local superó nueve pruebas automatizadas: integridad de datos, autenticación, contrato de inferencia y trace_id, cuatro entradas inválidas, escenario comercial, reglas SLO y salud no disponible. La evaluación usa 452 registros históricos sin ajustar el modelo. La recarga MLflow fue idéntica.
La prueba Docker confirmó despliegue inicial, reconciliación idempotente, recuperación de un contenedor detenido, rechazo de un candidato no listo y rollback después de dos ventanas lentas. El archivo despliegue.json conserva las observaciones; auditoria.jsonl conserva las decisiones. Las corridas de GitHub y sus artefactos permiten verificar la ejecución independiente. El resultado local no reemplaza la comprobación del estado de Actions.

## Reproducción y límites

Requisitos: Python 3.12, Docker y memoria suficiente para instalar dependencias. Ejecutar pip install -r requirements.txt; python -m pytest pruebas -q; python scripts/evaluate.py; docker build -t vertice-fase3:local .; definir API_TOKEN mediante un secreto aleatorio de al menos 16 caracteres; python scripts/run_demo.py --image vertice-fase3:local. Para el tablero: streamlit run app.py.
La API escucha en loopback 18083. El contenedor usa un usuario sin privilegios, dos CPU y 1 GB como límites de laboratorio. No se versionan secretos ni el directorio runtime. Para abrir MLflow: mlflow ui --backend-store-uri runtime/mlruns. Antes de producción exigiría validación del dominio, derechos de uso del dataset, revisión de seguridad, supervisión humana y un entorno persistente con gestión centralizada de secretos.