# Cómo grabar la entrevista con mi voz

## Preparación

1. Ensayar [Teleprompter](Teleprompter.md) con cronómetro; objetivo 5–7 minutos. Las marcas son orientativas.
2. Abrir las ocho láminas con `python video/generar_fondo.py` y luego `video/fondo_presentacion.html`. Flechas derecha e izquierda cambian de lámina; pantalla completa del navegador ayuda a evitar distracciones. El HTML se genera localmente y se exportará con los entregables finales.
3. Usar OBS Studio desde [su sitio oficial](https://obsproject.com/). Su [guía inicial](https://obsproject.com/kb/quick-start-guide/) explica cómo combinar fuentes. En macOS, añadir **macOS Screen Capture** para la ventana de las láminas y **Video Capture Device** para la cámara. Añadir el micrófono como fuente de audio. No iniciar transmisión en vivo.
4. Colocar la cámara a la altura de los ojos, luz de frente y fondo sencillo. Reservar la esquina inferior derecha para mi imagen, sin tapar cifras. Cerrar notificaciones y cualquier ventana con información bancaria real.
5. Grabar una prueba de 20 segundos: escucharla con audífonos, comprobar que mi voz no sature y que las letras se lean. Dar personalmente a OBS los permisos de cámara, micrófono y pantalla que solicite macOS.

## Grabación

Elegir 1920×1080 y 30 fps si el equipo lo permite; 1280×720 también es suficiente. Grabar a archivo local, preferentemente MKV; usar Archivo → Remux de grabaciones para obtener MP4 al terminar. Leer las preguntas y responder con mi voz natural. Dejar pausas y mirar a cámara al explicar decisiones; no limitarme a leer cifras sin interpretarlas. Una toma completa facilita demostrar continuidad y dominio.

Las instrucciones de fuentes se apoyan en [captura de pantalla macOS](https://obsproject.com/kb/macos-screen-capture-source) y [cámara](https://obsproject.com/kb/video-capture-sources) de OBS. La configuración propuesta debe probarse en mi equipo.

## Verificación y sustitución

Guardar como `Entrevista_Eduardo_original.mp4`, fuera del archivo publicado, y compartirlo en este chat. No borrar todavía `Entrevista_FaseIII.mp4`.

```bash
ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,width,height -of json Entrevista_Eduardo_original.mp4
ffmpeg -v error -i Entrevista_Eduardo_original.mp4 -f null -
```

Comprobar duración de 300 a 420 segundos, imagen y audio presentes y ausencia de errores de decodificación. Escuchar principio, mitad y final; confirmar que las ocho preguntas y respuestas sean comprensibles. El análisis de codecs no puede verificar quién habla: Eduardo deberá confirmar que la grabación y la narración son propias.

Tras recibir y revisar la grabación, se reemplazará el MP4, se actualizará video_validacion.json y se retirarán las declaraciones de narración sintética de la documentación vigente. Mientras tanto, esas declaraciones permanecen y la autenticidad de una defensa personal sigue pendiente.
