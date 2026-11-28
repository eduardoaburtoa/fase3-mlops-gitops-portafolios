# Registro de versiones y procedencia

## Cadena del proyecto

| Componente | Revisión de origen | Qué se preserva |
|---|---|---|
| Modelo y umbral de Actividad 6 | [fefe906fbf915e30ee3673b7046ae9d95f35dba2](https://github.com/eduardoaburtoa/actividad6-evaluacion-portafolios/tree/fefe906fbf915e30ee3673b7046ae9d95f35dba2) | SVM calibrada, clase negativa y umbral 0.20 |
| API de Fase II | [b6ecb7a0e6b01ece989369b7b67178fe7d7cc2a4](https://github.com/eduardoaburtoa/fase2-despliegue-portafolios/tree/b6ecb7a0e6b01ece989369b7b67178fe7d7cc2a4) | Antecedente de integración por API |
| Observabilidad de Actividad 8 | [0477912e48c547a1fdf60b34d433d976a7e87648](https://github.com/eduardoaburtoa/actividad8-observabilidad-portafolios/tree/0477912e48c547a1fdf60b34d433d976a7e87648) | Antecedentes de SLO e incidentes; no todos sus componentes se incorporan |
| Gobierno y escala de Actividad 9 | [7985794d0e3fd47cc54e2c192a9201ca727d9b67](https://github.com/eduardoaburtoa/actividad9-escalabilidad-gobernanza/tree/7985794d0e3fd47cc54e2c192a9201ca727d9b67) | Snapshot fuente de backend, modelo, contexto y antecedentes |
| Primera integración Fase III | [1107f485](https://github.com/eduardoaburtoa/fase3-mlops-gitops-portafolios/commit/1107f485ec0c50af7237af7d0c6212aab499a66f) | Servicio, evaluación MLflow y CD académico |
| Segunda implementación validada | [772a1b39](https://github.com/eduardoaburtoa/fase3-mlops-gitops-portafolios/commit/772a1b39a9d25a015548004ff43a2904265f49df) | Documentos, video y ajustes de trazabilidad |
| Cierre auditado inicial | [9bc989bf](https://github.com/eduardoaburtoa/fase3-mlops-gitops-portafolios/commit/9bc989bfc33db84411d4b0adeee7b37ef993136b) | Evidencia de segunda corrida de Actions aprobada |

Fuentes: `modelos/manifest.json`, `evidencias/procedencia.json`, commits del repositorio y README de Actividad 6 en la revisión citada. Una referencia histórica no significa que se hayan copiado íntegramente todas las capacidades de esa entrega.

## Iteración que respalda el umbral

Actividad 6 utilizó 1,807 registros de desarrollo y 452 de test, después de deduplicar el corpus. Su README documenta cinco folds externos estratificados y tres internos para selección; TF-IDF se ajustó dentro de cada pipeline y la SVM se calibró dentro del entrenamiento. El umbral final se eligió con predicciones fuera de muestra de desarrollo, no optimizando el test.

La rejilla documentada va de 0.05 a 0.95 con paso 0.025. El criterio usa el costo didáctico 5×FN + FP sujeto a restricciones si resultan factibles; cuando no, conserva el mínimo de costo y declara la meta incumplida. La candidata académica quedó en 0.20. La meta conjunta de recall ≥90 % y precisión ≥60 % **no se alcanzó**. No convierto unidades de ese costo en pesos.

En la comparación retrospectiva publicada, bajar de 0.50 a 0.20 redujo omisiones de 21 a 10 y aumentó falsas alertas de 7 a 25. Es una lectura del antecedente, no una nueva selección realizada en Fase III. Mantener el artefacto congelado permite atribuir la recuperación observada a configuración e infraestructura, en lugar de mezclarla con cambios predictivos.

## Integridad y recuperación

El SHA-256 del modelo sigue siendo `f48c7496d5a12bd15d535721e3e83c6ef895b1ae7eaccbe7f4f4c60705bb1916`. Las nueve pruebas y la comparación de probabilidades en MLflow verifican continuidad funcional. La revisión documental no toca ese archivo, el umbral ni el código operativo.

Git recupera revisiones del código; MLflow conserva el modelo como artefacto de corrida; Docker y el reconciliador identifican el despliegue. No se implementó una promoción de versiones en Model Registry ni un almacén de imágenes de producción. La recuperación automática demostrada usa el estado previo disponible en el laboratorio.
