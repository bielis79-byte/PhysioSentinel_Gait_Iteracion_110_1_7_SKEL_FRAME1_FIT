# PhysioSentinel Gait · Iteración 105.5

- Añadido botón **Grabar ciclo** al visor V105.
- Captura exactamente el modo activo: **Rig**, **Huesos** o **Rig + Huesos**.
- Grabación autónoma en navegador mediante `canvas.captureStream()` + `MediaRecorder`.
- Reinicia al frame 1, reproduce un ciclo completo y detiene automáticamente la grabación.
- Descarga MP4/H.264 cuando Chrome lo expone; fallback WEBM (VP9/VP8).
- Nombre de archivo identifica el modo capturado.
- No modifica la cinemática, las métricas clínicas ni el retargeting de V105.4.
