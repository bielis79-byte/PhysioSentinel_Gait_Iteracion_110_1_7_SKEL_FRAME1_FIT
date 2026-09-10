# PhysioSentinel Gait · Iteración 89

## Objetivo
Dar un salto visual respecto a V88 y aproximar la representación a un atlas anatómico humano en movimiento, utilizando las dos cámaras cuando el análisis es biplanar.

## Cambios
- Nueva cuarta capa: **Atlas anatómico realista · experimental**.
- La capa se anima **frame a frame** con la reconstrucción 3D ya existente.
- En Nivel 2/3, la cinemática procede de la fusión **frontal + lateral**; la interfaz lo indica explícitamente.
- Mayor detalle óseo: columna segmentada, parrilla costal, esternón, clavículas, pelvis, cráneo/mandíbula, fémur, tibia/peroné, húmero, radio/cúbito, rótula y pie.
- Mayor diferenciación muscular superficial: glúteos, cuádriceps/vastos, cadena posterior/aductora, tibial anterior, peroneos, gastrocnemios/sóleo, deltoides, bíceps/tríceps, antebrazo, abdominales/pectorales/paravertebrales.
- Se mantiene reproducción directa en la pestaña 11, MP4 de vista fija, multivista y reproyección 2D.
- La nueva capa queda seleccionada por defecto en sesiones nuevas.
- No se modifican HALPE26, tracking, eventos, métricas biomecánicas, Supabase, reconstrucción 3D ni el hotfix OpenCV/RTMLib/ONNXRuntime.

## Límite metodológico
La geometría sigue siendo un **atlas genérico procedimental**, no una malla anatómica individual obtenida por RM/TAC. Para alcanzar acabado fotorrealista tipo atlas comercial sería necesario incorporar una malla 3D externa con licencia compatible y rigging/skinning.
