# V99 · Modo GPU seguro

La V99 está diseñada para que el atlas anatómico real pueda utilizarse con menor riesgo de saturar GPU/VRAM del equipo cliente.

## Uso recomendado

1. Mantener activado **🛡️ Modo GPU seguro (recomendado)**.
2. Abrir inicialmente **Huesos**. V99 no carga la musculatura hasta que se solicita.
3. Para revisar músculos, pulsar **Músculos**. En modo seguro el esqueleto se libera previamente de GPU.
4. Evitar `Ambos` en el equipo que presentó `VIDEO_SCHEDULER_INTERNAL_ERROR`.
5. Usar **Liberar GPU** al terminar de revisar el atlas, especialmente antes de repetir un análisis pesado.

## Política gráfica

- una capa anatómica residente a la vez;
- DPR 1;
- resolución interna máxima 1280×720;
- sin antialias;
- materiales Lambert ligeros;
- render sólo cuando hace falta;
- máximo 24 FPS durante animación;
- pausa automática si la pestaña queda oculta;
- `dispose()` explícito de geometrías/materiales/texturas.

## Importante

`VIDEO_SCHEDULER_INTERNAL_ERROR` es un error del subsistema gráfico de Windows. La app puede actuar como desencadenante al elevar la carga gráfica, pero V99 no sustituye una revisión/actualización del controlador de la GPU si el fallo vuelve a ocurrir.
