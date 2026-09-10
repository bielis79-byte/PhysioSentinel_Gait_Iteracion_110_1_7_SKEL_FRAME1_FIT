# PhysioSentinel Gait · Iteración 107

## Cambio de arquitectura

V107 abandona el retargeting dinámico de las 201 mallas del atlas BodyExplorer durante la reproducción. Se incorpora un recurso local propio `PhysioSentinel_Skeleton_Rigged_v1.glb` con jerarquía articular explícita y nodos estables para pelvis, tronco, cabeza y extremidades.

## Cinemática

- Fuente: secuencia XYZ V104.
- Política del visor V107: ciclo determinista de 75 frames. Si la fuente contiene otro número de instantes, se seleccionan 75 posiciones equiespaciadas a lo largo del ciclo completo, preservando inicio y final.
- Cada frame se calcula desde las coordenadas del paciente; no se acumulan transformaciones entre frames.
- Los nodos reciben matrices absolutas derivadas de los segmentos del rig y se convierten a matrices locales respecto de su padre.

## Visor

- `Rig`
- `Esqueleto`
- `Rig + Esqueleto`
- Reproducción, ±1, Reset, slider y reencuadre.
- Grabación del canvas y descarga MP4 cuando el navegador lo soporta; WEBM como alternativa.
- Modelo GLB embebido localmente en el componente, evitando la descarga del atlas óseo desde CDN en tiempo de ejecución.

## Alcance

`PhysioSentinel_Skeleton_Rigged_v1.glb` es el primer modelo óseo articulado propio de PhysioSentinel. Es un modelo segmentario pre-riggeado orientado a validar el retargeting estable; no equivale todavía al atlas anatómico completo de 201 mallas de BodyExplorer/Z-Anatomy ni incorpora musculatura.
