# Bitácora de decisiones verificables

Las fechas se expresan en America/Mexico_City. Esta bitácora es una reconstrucción documentada de commits y configuración, no un registro contemporáneo de conversaciones internas. Las alternativas no implementadas son evaluaciones de diseño hechas en esta revisión, salvo que exista evidencia histórica explícita.

| Fecha | Evidencia | Decisión observable | Alternativa y razón documentada |
|---|---|---|---|
| 26 noviembre 2026 | `1107f485` | Integrar API, MLflow y despliegue académico | No se reentrenó: el alcance era validar operación de un modelo construido |
| 26 noviembre 2026 | `772a1b39` | Añadir entregables y evidencias de ejecución | No presentar sólo código: el evaluador necesita resultados y explicación |
| 26 noviembre 2026 | `772a1b39`, CHANGELOG | Verificar autenticación en reconciliación y registrar excepciones | Una comprobación de salud sin credencial válida no bastaba para reusar un servicio |
| 26 noviembre 2026 | `99794334` | Publicar captura real de MLflow | La captura complementa el JSON; no sustituye la recarga verificable |
| 26 noviembre 2026 | `9bc989bf` | Conservar la segunda ejecución verde de Actions | No inferir éxito remoto a partir de una prueba local |
| 26 noviembre 2026 | PR 1, `fb1b7f42` | Preparar grabación personal sin borrar el video existente | No declarar voz del autor mientras el MP4 sea sintético |
| 26 noviembre 2026 | PR 2, `7b950be6` | Incorporar el business case y separar proyección de medición | No presentar ROI esperado como beneficio ya generado |
| 26 noviembre 2026 | PR 3 | Profundizar documentación sin modificar ingeniería | No reentrenar ni alterar las nueve pruebas para aumentar la apariencia de alcance |

## Iteraciones conservadas

La primera invocación local del ensayo no encontró la imagen porque la construcción aún no terminaba. Se repitió después de completar el build. Ese antecedente figura en CHANGELOG; no se dispone de una captura contemporánea de ese intento y no la reconstruyo como si existiera.

El primer registro MLflow carecía de firma. La segunda aproximación con lista produjo una advertencia de inferencia de firma; la versión final usa un ejemplo NumPy y firma explícita. Los tres registros se conservaron en el seguimiento local. Esto fue una iteración del empaquetado y trazabilidad, no una nueva SVM ni un cambio de umbral.

GitHub muestra advertencias de deprecación de Node.js 20 en acciones de terceros y las pruebas locales avisaron sobre httpx en Starlette. Las ejecuciones terminaron correctamente. Dejo ese mantenimiento pendiente sin alterar el pipeline aprobado, conforme al alcance de esta revisión.

## Qué prueban las capturas

Las capturas de Actions muestran los dos trabajos aprobados de las corridas originales 45922494111 y 45924738199. Docker Desktop muestra el contenedor vertice-fase3-api activo y el puerto local 18083. Son capturas obtenidas durante esta revisión, no del instante original de cada despliegue. Su publicación binaria corresponde a la exportación final para respetar el protocolo de ramas de texto.

Los indicadores de CPU y memoria de una captura son instantáneos y pueden incluir otros componentes del motor. No los uso como benchmark ni los incorporo a las métricas del documento.
