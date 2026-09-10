# V101 · Atlas anatómico 3D con rig jerárquico

V101 corrige el desmontaje del atlas observado en V100. El principio de implementación es que cada malla anatómica se vincula una sola vez a un nodo de segmento en pose de reposo. Durante la reproducción se modifican los nodos, no se recolocan las mallas individualmente.

La cinemática se expresa como transformaciones relativas al primer frame válido. En los segmentos hijos se elimina la contribución del padre antes de aplicar la rotación local. Esto reduce el riesgo de dobles transformaciones y separación de huesos.

La opción `Mostrar rig` superpone la estructura cinemática para verificar continuidad. `Paso +1` permite inspección frame a frame.

## Vídeo

`Grabar ciclo` reproduce y captura un ciclo completo del canvas. El navegador selecciona el formato disponible: MP4/H.264 cuando `MediaRecorder` lo soporta y WEBM como alternativa. Al terminar aparece el enlace `Descargar vídeo` dentro del visor.

## Alcance

Las geometrías son anatómicas reales de la fuente configurada, pero la asignación de mallas y los pivotes continúan siendo un rig genérico estimado. No es skinning de vértices ni anatomía individual del paciente.
