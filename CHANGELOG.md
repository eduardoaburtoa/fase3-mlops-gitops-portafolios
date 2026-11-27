# Bitácora de Fase III

## 1.0.0 · 26 de noviembre de 2026

- Conservé el modelo y umbral de Actividad 6 y documenté los commits de continuidad.
- Integré validación de integridad, contratos de API y reglas de negocio.
- Registré una reevaluación real en MLflow y comprobé recarga idéntica.
- Construí y ejecuté Docker localmente; probé deriva de estado, candidato no listo y retardo de 400 ms con rollback.
- Publiqué CI y CD académico: primera corrida completa 45922494111 aprobada en GitHub Actions.
- Corregí la comprobación de autenticación en la reconciliación y el registro de excepciones del middleware.
- Validé las cinco vistas de Streamlit y produje documentos PDF, Word y Google Docs, más una entrevista MP4 con narración sintética.

### Iteraciones y límites

La primera invocación local del experimento se adelantó al final de la construcción de la imagen y falló sin desplegar; se repitió después de completar el build. El primer registro MLflow no incluía firma; se agregó un ejemplo NumPy y firma explícita tras detectar una incompatibilidad de inferencia con una lista convertida a tabla. La reevaluación final pasó sin esa advertencia. Las pruebas emitieron una advertencia de deprecación de httpx en Starlette; no produjo fallos, pero queda como mantenimiento del entorno.

El despliegue de Actions termina con su ejecutor. No existe un servicio de producción persistente ni una validación prospectiva de rentabilidad. La autorización de producción permanece desactivada.
