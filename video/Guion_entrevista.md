# Simulación de entrevista profesional

Eduardo Aburto Angulo · Fase III

Voces sintéticas del sistema. No reproduce la voz real del autor.

## Presentación del proyecto

**Entrevistador:** ¿Qué problema resuelve Vértice AI?

**Eduardo — guion dramatizado:** Soy Eduardo Aburto Angulo. Presento un asistente de preparación de revisiones de portafolio. Desde mi enfoque de banquero sénior, busco llegar a cada conversación con señales claras y evidencia que pueda explicar. El prototipo clasifica noticias financieras negativas para priorizar una revisión humana. No recomienda automáticamente comprar o vender un fondo. Esta presentación es una simulación de entrevista con voces sintéticas y reúne resultados reales de ejecución en un laboratorio académico.

## Arquitectura de la solución

**Entrevistador:** ¿Cómo integraste el modelo con la operación?

**Eduardo — guion dramatizado:** Conservé la máquina de vectores de soporte calibrada y el umbral de cero punto veinte de la actividad seis. FastAPI ofrece contratos de entrada y salida. Docker empaqueta el servicio; MLflow conserva parámetros, métricas y el modelo. Streamlit presenta los resultados. El repositorio incorpora una configuración declarativa del despliegue. Separé la decisión financiera de la señal técnica: una noticia negativa inicia análisis, pero no autoriza una operación.

## Pipeline y GitOps

**Entrevistador:** ¿Qué sucede cuando publicas un cambio?

**Eduardo — guion dramatizado:** La automatización de GitHub primero valida los datos y el código. Comprueba hashes, contratos de la API, entradas inválidas y las reglas operativas. Después reevalúa el modelo congelado y verifica que la recarga desde MLflow produzca las mismas predicciones. Si pasa esa etapa, construye una imagen identificada por el commit y despliega el contenedor en un ejecutor temporal. El reconciliador compara el estado esperado y verifica salud y versión antes de aceptar la entrega. Es una implementación académica de GitOps, no un clúster de producción.

## Resultados del modelo

**Entrevistador:** ¿Qué evidencia respalda su desempeño?

**Eduardo — guion dramatizado:** Reevalué cuatrocientas cincuenta y dos noticias financieras en inglés. La exactitud fue de noventa y dos punto veintiséis por ciento y el F uno fue cero punto setenta y cuatro. Hubo diez falsos negativos y veinticinco falsos positivos. Los primeros pueden omitir noticias que merecen revisión; los segundos agregan trabajo. No cambié el umbral usando el test. Tampoco interpreto estas métricas como evidencia de rentabilidad en fondos mexicanos. La adaptación a ese dominio sigue siendo una validación pendiente.

## Incidentes y recuperación

**Entrevistador:** ¿Cómo sabes que el sistema puede recuperarse?

**Eduardo — guion dramatizado:** Ejecuté dos incidentes controlados. Primero inicié un candidato que no superaba la comprobación de salud. El reconciliador lo rechazó y restauró la configuración anterior. Después inyecté cuatrocientos milisegundos de retardo. Dos ventanas consecutivas incumplieron el objetivo de latencia y dispararon el retorno a la configuración estable. El percentil noventa y cinco pasó de cerca de cinco milisegundos a más de cuatrocientos veintiséis y se recuperó a cerca de siete. Conservé los errores y el consumo del presupuesto; recuperarse no borra el incumplimiento anterior.

## Negocio y responsabilidad

**Entrevistador:** ¿Cómo manejas el incentivo por comisiones?

**Eduardo — guion dramatizado:** El interés del cliente debe orientar la revisión. Usé ciento cincuenta clientes ficticios con posiciones de cinco a veinte millones de pesos para no trabajar con información confidencial. El uno por ciento de compra y el uno por ciento de venta son supuestos académicos, no una tarifa verificada de BBVA. Una revisión sólo sería elegible si preserva el perfil y el beneficio incremental supuesto es positivo después de costos. Las comisiones no justifican una rotación innecesaria. No ejecutamos operaciones y la autorización de producción permanece desactivada.

## Decisiones de gestión

**Entrevistador:** ¿Qué falta para un uso real en la industria?

**Eduardo — guion dramatizado:** Antes de ampliar el alcance exigiría derechos de uso de los datos, evaluación prospectiva en español, revisión de idoneidad y supervisión humana. En infraestructura faltan almacenamiento durable de observabilidad, secretos administrados, firma de imágenes y pruebas de carga sostenidas. El contenedor único puede interrumpir el servicio durante un reemplazo. La demostración de despliegue continuo es temporal; no equivale a un servicio público permanente ni a alta disponibilidad. Explicar estos límites forma parte de la responsabilidad técnica.

## Siguiente hito

**Entrevistador:** ¿Cómo medirías el valor del siguiente piloto?

**Eduardo — guion dramatizado:** Propondría un piloto en sombra, sin órdenes de inversión. Compararía tiempo de preparación, cobertura de señales y utilidad de la revisión frente a una línea base, con etiquetas independientes y análisis por perfil e idioma. Sólo después evaluaría beneficios netos para el cliente y costo operativo. Mi conclusión es que el proyecto demuestra una entrega verificable: código, modelo, monitoreo, recuperación y narrativa profesional. El siguiente avance debe estar respaldado por nueva evidencia, no sólo por una interfaz más atractiva.