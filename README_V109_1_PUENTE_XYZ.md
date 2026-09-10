# V109.1 — Puente V104/V107 → SKEL

Esta iteración no intenta todavía resolver los parámetros de pose SKEL. Su único objetivo es verificar que el motor cinemático de PhysioSentinel entrega correctamente los landmarks 3D del paciente al futuro optimizador SKEL.

El panel selecciona el primer frame con suficiente cobertura, exporta sus XYZ y lo representa en 3D. Si la entrada es correcta, la siguiente versión puede concentrarse exclusivamente en el fit SKEL.
