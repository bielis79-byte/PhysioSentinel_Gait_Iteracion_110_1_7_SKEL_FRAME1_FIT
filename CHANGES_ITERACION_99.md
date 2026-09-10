# PhysioSentinel Gait · Iteración 99.0

## Objetivo
Reducir de forma agresiva la presión sobre GPU/VRAM y memoria del navegador del visor anatómico 3D, después de observar un reinicio de Windows con `VIDEO_SCHEDULER_INTERNAL_ERROR` durante las pruebas de V98.

## Cambios V99

- **Modo GPU seguro activado por defecto** en la pestaña 11.
- Carga inicial de **sólo el esqueleto**; la musculatura se descarga/carga únicamente cuando el usuario pulsa `Músculos`.
- En modo seguro se mantiene **una sola capa anatómica residente en GPU**. Al cambiar Huesos ↔ Músculos se liberan geometrías, materiales y texturas de la capa anterior.
- `Ambos` queda deshabilitado en modo seguro para evitar mantener simultáneamente las ~668 mallas del atlas.
- Nuevo botón **Liberar GPU** para descargar explícitamente ambas capas del contexto WebGL.
- WebGL de bajo consumo: `powerPreference='low-power'`, antialias desactivado, stencil desactivado, `preserveDrawingBuffer=false`.
- `devicePixelRatio` fijado a 1 en modo seguro y resolución interna limitada a 1280×720.
- Materiales PBR del atlas reemplazados, en modo seguro, por **MeshLambertMaterial** conservando el color base para disminuir complejidad de shaders y uso de texturas.
- Render **bajo demanda** cuando el atlas está estático: ya no se mantiene un `requestAnimationFrame` continuo sin necesidad.
- Animación limitada a **24 FPS máximos**.
- La reproducción se detiene automáticamente cuando la pestaña/documento deja de estar visible.
- Gestión explícita de `webglcontextlost` / `webglcontextrestored`.
- Liberación de geometrías/materiales/texturas y del renderer al abandonar el iframe (`pagehide`).
- Diagnóstico del visor muestra geometrías/texturas WebGL y política GPU activa.

## Sin cambios

- HALPE26 / RTMLib / OpenVINO.
- Análisis biomecánico 2D.
- Fusión biplanar y cálculos clínicos.
- V48–V52.
- Supabase.
- Fuentes anatómicas BodyExplorer/BodyParts3D/Z-Anatomy.

## Alcance
V99 reduce la carga que PhysioSentinel impone al navegador/GPU, pero no puede garantizar que un controlador gráfico o una GPU inestable no vuelva a producir un BSOD. Si reaparece `VIDEO_SCHEDULER_INTERNAL_ERROR`, debe revisarse también el driver y el hardware gráfico.
