# PhysioSentinel Gait V107.1

- Mantiene el GLB local pre-riggeado de V107 y el ciclo V104 determinista de 75 frames.
- Corrige el retargeting: cada nodo usa `desired(t) * inverse(desired(rest)) * modelRestWorld`.
- Las matrices de reposo del GLB se capturan una sola vez tras cargar el modelo.
- No existe acumulación entre frames ni sustitución de las proporciones/offsets originales del GLB.
- En `Rig + Esqueleto`, los puntos cian son el rig V104 y los puntos magenta los orígenes articulares del modelo para auditar el registro.
- Material óseo claro para mejorar visibilidad.
- Corrige el NameError del bloque de auditoría heredado: usa la secuencia V107 activa y acceso seguro a metadatos V96.
- Mantiene grabación y descarga de vídeo.
