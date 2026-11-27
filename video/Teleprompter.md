# Entrevista con voz propia

Eduardo Aburto Angulo · Fase III · Guion para grabación personal pendiente.

**Duración objetivo: 6:40.** Dieciséis bloques de 25 segundos. Los tiempos son una pauta de ensayo, no mediciones de una grabación. Lee la pregunta al cambiar de lámina y responde mirando a cámara. Cada [pausa] dura aproximadamente un segundo. Ajusta la velocidad en el ensayo, sin acelerar las cifras. El video sintético publicado permanece identificado hasta recibir y verificar el MP4 personal.

## Lámina 1 — Qué problema resuelvo

**00:00–00:25**
Soy Eduardo Aburto Angulo, banquero patrimonial sénior, con veinte años en banca. [pausa] Mi proyecto es un asistente para preparar revisiones de portafolio. Quiero llegar a cada conversación con señales claras y argumentos que pueda explicar. La IA no sustituye el criterio del banquero; lo aumenta.

**00:25–00:50**
El problema es priorizar la revisión sin confundir una noticia con una orden. [pausa] El modelo identifica noticias financieras negativas en inglés. Esa señal inicia análisis; no autoriza comprar ni vender. Mi responsabilidad sigue siendo revisar el contexto, la idoneidad y el impacto neto para el cliente.

## Lámina 2 — Cómo integré la solución

**00:50–01:15**
Conservé la SVM calibrada de Actividad 6 y el umbral cero punto veinte. [pausa] FastAPI define contratos de entrada y salida; Docker empaqueta el servicio. MLflow registra el modelo y sus métricas. Streamlit facilita la lectura de resultados. Cada componente responde a una necesidad de operación verificable.

**01:15–01:40**
Git conserva el código y el estado deseado del despliegue. Un hash fija los bytes del modelo. [pausa] Esa separación me permite saber qué versión estoy usando y recuperar una configuración anterior. No volví a entrenar ni a elegir el umbral con el conjunto de prueba durante esta fase.

## Lámina 3 — Qué ocurre con un cambio

**01:40–02:05**
La automatización primero valida datos y código. Comprueba hashes, etiquetas, identificadores y posiciones simuladas. También verifica autenticación y entradas inválidas. [pausa] Después reevalúa el modelo y comprueba que la recarga desde MLflow produzca probabilidades idénticas. Si falla una condición, el despliegue no continúa.

**02:05–02:30**
Si la validación pasa, construye una imagen identificada por el commit. El reconciliador inicia el contenedor y comprueba salud y versión. [pausa] Es un despliegue funcional en un ejecutor temporal. No lo presento como un alojamiento permanente ni como un servicio bancario de alta disponibilidad.

## Lámina 4 — Qué resultados puedo defender

**02:30–02:55**
Reevalué cuatrocientas cincuenta y dos noticias. La exactitud fue noventa y dos punto veintiséis por ciento y el F uno, cero punto setenta y cuatro. [pausa] Hubo diez falsos negativos y veinticinco falsos positivos. Un falso negativo omite una señal; un falso positivo aumenta el trabajo de revisión.

**02:55–03:20**
Estas métricas respaldan el funcionamiento sobre ese test histórico. No demuestran rentabilidad en fondos mexicanos. [pausa] La adaptación de idioma y dominio sigue pendiente. Tampoco confundo probabilidades de noticias negativas con probabilidad de pérdida de un fondo: son problemas distintos y necesitan validaciones distintas.

## Lámina 5 — Cómo respondí a incidentes

**03:20–03:45**
Probé dos incidentes controlados. Un candidato no superó la comprobación de salud y fue rechazado. Después inyecté cuatrocientos milisegundos de retardo. [pausa] Dos ventanas consecutivas incumplieron el objetivo y activaron el retorno a la configuración estable. La auditoría conserva las decisiones y sus tiempos.

**03:45–04:10**
El percentil noventa y cinco pasó de cerca de cinco milisegundos a más de cuatrocientos veintiséis, y se recuperó a cerca de siete. [pausa] Recuperarse no borra el consumo del presupuesto de error. El laboratorio usa un contenedor; reemplazarlo puede interrumpir brevemente el servicio. Ese límite queda documentado.

## Lámina 6 — Qué valor de negocio espero

**04:10–04:35**
El business case de Fase I plantea veinticuatro asesores y tres mil seiscientos clientes. Su ROI esperado a tres años es doscientos noventa y ocho punto seis por ciento. [pausa] Son proyecciones, no beneficios realizados. La condición central es que el cliente conserve un peso con cuatro centavos por cada peso de corretaje.

**04:35–05:00**
Si esa relación deja de ser positiva, debo revisar la viabilidad. El uno por ciento de compra y el uno por ciento de venta son supuestos académicos, no tarifas BBVA verificadas. [pausa] Las comisiones no justifican rotación innecesaria. Los clientes son ficticios y una revisión debe preservar el perfil y el beneficio neto supuesto.

## Lámina 7 — Qué falta para producción

**05:00–05:25**
La autorización de producción permanece desactivada. El corpus tiene licencia no comercial, y necesito resolver derechos antes de otro uso. [pausa] También faltan evaluación prospectiva en español, secretos administrados, observabilidad durable y pruebas de carga sostenidas. No atribuyo al prototipo capacidades que aún no probé.

**05:25–05:50**
En una entrevista técnica defendería evidencia reproducible, gobierno y respuesta a fallas, no sólo exactitud. [pausa] MLOps conecta calidad con operación; GitOps aporta control de cambios. Mi siguiente mejora sería decidir promociones con evidencia de dominio y riesgo. Firmas de imágenes y revisión independiente son propuestas pendientes, no logros actuales.

## Lámina 8 — Cuál es el siguiente paso

**05:50–06:15**
Propongo el piloto de nueve meses con seis asesores previsto en Fase I. En sombra, sin órdenes automáticas, compararía tiempo de preparación y utilidad de las señales contra una línea base. [pausa] El presupuesto previsto es nueve millones ochenta y tres mil cuatrocientos cuarenta y ocho pesos. La arquitectura funcionando no materializa por sí sola el ROI.

**06:15–06:40**
Mi conclusión es que ahora puedo explicar qué versión opero, cómo la valido y cómo respondo cuando falla. [pausa] El siguiente paso debe aportar evidencia de valor para el cliente y de costo operativo. Mantengo el ánimo de llevarlo a un piloto responsable, con una regla: la IA no sustituye el criterio del banquero; lo aumenta.
