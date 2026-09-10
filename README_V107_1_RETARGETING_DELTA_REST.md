# V107.1 · Retargeting por delta de reposo

Esta versión no cambia la arquitectura estable de V107. El GLB conserva su jerarquía y sus pivotes. La pose de cada segmento se deriva del cambio observado en el rig V104 respecto al frame 0 y se aplica sobre la matriz mundial de reposo del nodo del modelo.

Fórmula: `M_target(t) = M_rig(t) · inverse(M_rig(rest)) · M_model(rest)`.

El modo `Rig + Esqueleto` superpone además los orígenes articulares del modelo en magenta para facilitar la validación frame a frame.
