# PhysioSentinel Gait · Iteración 89.1

## Corrección principal
- La pestaña 11 informa de forma explícita si el atlas está disponible, parcial o no generado.
- Los fallos de reconstrucción/render dejan una causa concreta visible en la interfaz.
- La exportación ZIP crea siempre `04_ATLAS_ANATOMICO_3D/ESTADO_ATLAS.json`.
- Si el atlas existe, la carpeta incluye también coordenadas 3D, PNG y los MP4 disponibles (vista fija, multivista y reproyección 2D).
- Si el atlas no existe, la carpeta incluye un estado negativo y un `LEEME.txt` con la causa, evitando exportaciones ambiguas.
- La capa por defecto de exportación pasa a `Atlas anatómico realista · experimental` cuando no existe una selección previa.

## Sin cambios
- HALPE26, tracking, segmentación IC/TO, métricas biomecánicas y Supabase.
- Motor OpenCV/RTMLib/ONNX Runtime de V86.6.
- Convención de signos V75.

## Alcance metodológico
El atlas continúa siendo una representación anatómica genérica articulada con la cinemática estimada del paciente. No representa anatomía interna individual obtenida por RM/TAC y no estima EMG, activación, fuerza, tono ni volumen muscular.
