# V110.1.6 · prueba SKEL de un frame

1. Arranca la app.
2. Abre el panel SKEL.
3. Sube `skel_models_v1.1.zip`.
4. Selecciona `male` o `female`.
5. La app instalará el código SKEL público en `/tmp` sin dependencias y extraerá sólo el PKL privado elegido a otro directorio temporal.
6. El criterio de éxito es el mensaje `Primer forward SKEL REAL completado en CPU para 1 frame`.

Si falla, copia exclusivamente el bloque de error mostrado por V110.1.6; ya no es necesario volver a diagnosticar NumPy/OpenSim/BodyExplorer.
