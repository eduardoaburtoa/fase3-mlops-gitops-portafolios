# Portfolio técnico estratégico de Vértice AI

Eduardo Aburto Angulo · Fase III

## Problema y propuesta de valor

Como banquero Sr., quiero llegar a la revisión de portafolio con señales claras, fuentes identificables y argumentos que pueda explicar al cliente. La solución organiza una señal de noticias negativas para priorizar revisión humana. El valor potencial es reducir el tiempo de preparación y hacer más consistente el seguimiento; todavía no medí ahorro operativo ni rentabilidad incremental en clientes reales.
El caso conserva 150 clientes ficticios con nombres de superhéroes y villanos y posiciones de 5 a 20 millones de pesos. Esta elección permite dar personalidad a los escenarios sin utilizar datos confidenciales. El contexto es didáctico y no representa una cartera real ni una implementación oficial de BBVA.

## Trayectoria y decisiones

Actividad 4 exploró modelos preentrenados; Actividad 5 desarrolló entrenamiento trazable; Actividad 6 evaluó umbrales y generalización. Fase II integró API y contenedores. Actividad 8 agregó observabilidad e incidentes y Actividad 9 revisó costos y gobernanza. En Fase III integré un flujo de validación y despliegue continuo académico con evidencia reproducible.
La decisión principal fue conservar el modelo y el umbral mientras construía la operación. Así evité mezclar mejora del algoritmo con cambios de infraestructura. El test histórico sirve para verificar regresiones, no para escoger nuevas configuraciones. Elegí FastAPI por sus contratos, Docker por portabilidad, MLflow por trazabilidad y Streamlit por acceso sencillo a resultados.

## Resultados y alcance demostrado

El modelo congelado obtuvo F1 0.7445 y ROC-AUC 0.9548 en 452 registros; la recarga desde MLflow reprodujo exactamente sus probabilidades. Nueve pruebas locales aprobaron los contratos implementados. El contenedor recuperó su operación después de un candidato no listo y de una latencia inducida. La última ventana quedó debajo del límite de 250 ms.
Estas evidencias muestran que el prototipo puede probarse, desplegarse y recuperarse en laboratorio. No prueban rentabilidad, idoneidad regulatoria, disponibilidad mensual ni escalabilidad ante demanda real. Presento también los límites porque una decisión profesional necesita distinguir lo medido de lo esperado.

## Economía y gobierno responsable

El escenario comercial calcula beneficio incremental supuesto, costos adicionales y corretaje de 1 % por compra más 1 % por venta sobre el nocional migrado. Esa comisión es un supuesto académico, no una tarifa corroborada de BBVA. Los gastos deben incluirse sólo si no están ya descontados de la rentabilidad para evitar doble conteo. No equiparo ingreso bruto por comisiones con utilidad neta del banco.
Una revisión sólo se considera elegible si conserva el perfil y el beneficio neto supuesto es positivo. El incentivo comercial no debe justificar rotación innecesaria. Antes de uso real exigiría consentimiento, revisión de idoneidad, verificación de cada ficha y serie, derechos de uso de datos, supervisión humana y seguimiento del resultado neto del cliente. La autorización de producción permanece desactivada.

## Presentación profesional y siguientes pasos

La entrevista adjunta expone el problema, la arquitectura, la evidencia de recuperación, los límites del modelo y los criterios de gobierno. Es una dramatización con voces sintéticas y guion en primera persona, no una grabación de mi voz ni una entrevista real. El guion permite preparar una defensa personal y responder preguntas técnicas o de gestión.
Mi siguiente hito sería una evaluación prospectiva en sombra: señales sin operaciones, etiquetado independiente, métricas por perfil e idioma y medición de tiempo de preparación frente a una línea base. Sólo después decidiría si existe beneficio suficiente para ampliar el piloto. El objetivo de esta fase es demostrar disciplina de entrega y capacidad de comunicar las decisiones con evidencia.