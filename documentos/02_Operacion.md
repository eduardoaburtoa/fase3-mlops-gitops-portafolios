# Operación y validación del servicio de portafolios

Eduardo Aburto Angulo · Fase III

## Arquitectura y responsabilidades

La solución reúne API FastAPI, SVM calibrada, seguimiento MLflow, monitor por ventanas, reconciliador Docker y tablero Streamlit. El modelo clasifica noticias financieras en inglés; una probabilidad negativa igual o superior a 0.20 prioriza revisión humana. La salida no estima rendimientos ni indica el fondo que se debe comprar.
Como responsable del caso de negocio, revisaría la utilidad y pertinencia de cada señal. El responsable técnico custodia versiones y atiende incidentes; el responsable del modelo valida etiquetas y deriva; cumplimiento decide sobre privacidad, derechos de datos y alcance permitido. Es una propuesta de responsabilidades, no una designación de personal real.

## Contratos de observabilidad

Cada solicitud recibe un trace_id generado por el servicio. El log registra ruta normalizada, método, estado, duración y hash del modelo, sin guardar el texto enviado, nombres de clientes o credenciales. /v1/metrics exige autenticación y devuelve contadores y hasta 2 000 latencias recientes en memoria. Estos datos se reinician con el proceso; no sustituyen una plataforma durable de observabilidad.
Las trazas son identificadores de correlación locales; no implementé trazas distribuidas OpenTelemetry. La latencia del experimento se mide en el cliente con reloj monotónico, incluida la ida y vuelta HTTP. El contador de errores del servidor incluye estados 5xx; el monitor también incluye fallos de transporte. Los 4xx deben investigarse como errores de contrato y el ensayo exige respuestas 200.

## Indicadores y presupuesto de error

Definí disponibilidad de 99 % y 99 % de solicitudes con latencia no mayor de 250 ms, en ventanas de al menos 20 observaciones. Presupuesto permitido = N × 0.01. Consumo relativo = eventos malos / presupuesto permitido. Dos ventanas consecutivas incumplidas disparan la alerta P2 de latencia. Estos objetivos describen el laboratorio y no equivalen a un SLA mensual.
En las 80 solicitudes de las cuatro ventanas hubo 40 lentas por la inyección deliberada. El presupuesto de latencia era 0.8 solicitudes; el consumo relativo fue 50 veces y el saldo fue −39.2. La recuperación final no borra ese incumplimiento histórico. Todas las solicitudes de inferencia del ensayo respondieron 200; los sondeos de salud fallidos del candidato se conservan en la auditoría de despliegue y no se suman al denominador de inferencias.

## Runbooks y resultados

RB01, candidato no listo: detener la promoción, conservar la versión activa, restaurarla y verificar salud y hash. El ensayo inyectó FAIL_READINESS=1 y confirmó rollback_recovered=true. Si no existe versión saludable anterior, el reconciliador falla explícitamente y requiere intervención.
RB02, latencia persistente: confirmar dos ventanas incumplidas, registrar alerta P2, restaurar la configuración anterior y medir otra ventana. El p95 pasó de 5.45 ms en referencia a 426.24 y 426.46 ms con retardo; después del rollback fue 6.60 ms. Son mediciones locales de esta ejecución, no capacidad garantizada. Ante fallos persistentes mantendría el servicio fuera de uso y escalaría al responsable técnico.

## Calidad auditoría y optimización

La reevaluación preserva accuracy 0.9226, precision 0.6711, recall 0.8361, F1 0.7445 y ROC-AUC 0.9548. Los 10 falsos negativos representan noticias negativas omitidas; los 25 falsos positivos añaden trabajo de revisión. La cobertura lingüística y el cambio de dominio son límites materiales. El seguimiento de calidad futura requiere etiquetas independientes; una variación en entradas no prueba por sí sola degradación de desempeño.
La optimización implementada evita recrear contenedores cuando el estado ya coincide, limita recursos y reduce alertas por persistencia de dos ventanas. Los antecedentes de batching y fairness se conservan identificados como históricos, sin atribuirles una nueva medición. Priorizaría luego almacenamiento durable, métricas por cohortes, pruebas de carga sostenidas, firma de imágenes y un despliegue de dos instancias antes de afirmar preparación industrial.