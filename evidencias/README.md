# Evidencias verificables

[Portada](../README.md) · [Documentación](../documentos/README.md)

| Evidencia | Qué permite comprobar |
|---|---|
| [GitHub Actions](github_actions.json) | Validación y despliegue continuo completos en un ejecutor temporal |
| [Evaluación MLflow](evaluacion.json) | Cinco métricas, matriz de confusión, corrida y recarga idéntica |
| [Pruebas locales](tests.xml) | Nueve pruebas automatizadas aprobadas |
| [Experimento Docker](despliegue.json) | Salud, idempotencia, recuperación de estado y dos incidentes |
| [Auditoría](auditoria.jsonl) | Secuencia temporal de despliegues y rollback, sin secretos |
| [Latencia](latencia.png) | Comparación antes, durante y después del retardo inyectado |
| [Streamlit](streamlit.png) | Captura real del tablero local |
| [Procedencia](procedencia.json) | Repositorios y commits de continuidad |

Las mediciones son de laboratorio. Las cuatro ventanas incluyen 80 inferencias y 40 lentas por la inyección deliberada. La recuperación no elimina el consumo del presupuesto. La carpeta antecedentes conserva resultados históricos identificados como tales.

[Segunda ejecución local](despliegue_revision_final.json): confirmó otra vez el ciclo completo con la versión corregida. El reporte y la gráfica mantienen la primera medición de despliegue.json; container_logs.jsonl corresponde a la segunda ejecución y contiene únicamente registros JSON estructurados. La auditoría conserva la secuencia de ambas corridas.
