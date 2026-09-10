# PhysioSentinel Gait · Iteración 87

- Mantiene intacta la cadena de análisis biomecánico, HALPE26, tracking, Supabase y hotfix OpenCV/RTMLib de V86.6/V86.7.
- Sustituye visualmente el avatar V86 por una anatomía genérica articulada más detallada.
- Esqueleto: huesos dobles aproximados en pierna (tibia/peroné) y antebrazo (radio/cúbito), articulaciones diferenciadas, pelvis, columna, caja torácica, clavícula visual, cráneo y pies.
- Modelo musculoesquelético: fascículos visuales separados para muslo, pierna, glúteos, brazo/antebrazo y tronco, todos articulados frame a frame con la cinemática reconstruida.
- La pestaña 11 reproduce directamente el MP4 del avatar en movimiento con autoplay/loop; ya no se limita a una previsualización estática y botones de descarga.
- Añade reproducción directa del vídeo multivista y de la reproyección 2D.
- Limitación: anatomía genérica paramétrica, no segmentación ósea/muscular individual del paciente, no EMG, no fuerza ni volumen muscular medido.
