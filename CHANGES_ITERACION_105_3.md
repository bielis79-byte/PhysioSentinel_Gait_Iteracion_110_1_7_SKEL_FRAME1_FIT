# PhysioSentinel Gait V105.3

Hotfix de visibilidad del visor Rig + Atlas óseo.

- Normaliza el atlas BodyExplorer y el rig XYZ V104 a una escala visual corporal común (~2.8 unidades).
- Centra atlas y rig en el mismo espacio visual antes del autoencuadre.
- Recalcula near/far de cámara dinámicamente para evitar clipping completo del atlas.
- Reencuadra automáticamente al cambiar entre Rig, Huesos y Rig + Huesos.
- Añade diagnóstico de tamaño nativo XYZ y factores de escala visual.
- Conserva los 75 frames originales, GPU SAFE, fallback de carga y retargeting desde pose de referencia.
