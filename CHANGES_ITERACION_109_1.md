# PhysioSentinel Gait V109.1

## Corrección principal
V109 mostraba 75 frames disponibles pero 0 landmarks objetivo. V109.1 sustituye el extractor del PoC por un puente XYZ tolerante a las estructuras reales de V104/V107.

- Lee prioritariamente `frame['joints']`, formato oficial del payload V104/V107.
- Acepta listas, tuplas, `numpy.ndarray`, `pandas.Series` y diccionarios XYZ.
- Normaliza alias de nombres articulares.
- Selecciona automáticamente el primer frame con cobertura articular suficiente en vez de asumir que el frame 1 siempre es completo.
- Deriva únicamente el centro `Hip` si existen ambas caderas; queda marcado como derivado y no modifica métricas clínicas.
- Añade visor 3D del frame objetivo y tabla XYZ antes de conectar SKEL.
- Los archivos privados SKEL siguen siendo opcionales en esta etapa.

## Criterio de paso a V110
No avanzar al ajuste SKEL hasta que el panel muestre al menos 10 landmarks válidos y la geometría del frame objetivo sea coherente visualmente.
