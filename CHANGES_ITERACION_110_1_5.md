# PhysioSentinel Gait · V110.1.5

Hotfix del runtime SKEL CPU en Streamlit Cloud.

- Corrige `Permission denied` al intentar instalar SKEL bajo demanda en el `site-packages` del entorno administrado.
- SKEL se instala con `pip --no-deps --target` en `/tmp/physiosentinel_skel_cpu_v110_1_5`, ruta escribible y aislada.
- Añade el target temporal a `sys.path` y reutiliza una marca `.ready` durante la vida de la instancia.
- Mantiene NumPy 2.x para Pose2Sim/OpenSim y no instala `moderngl-window`.
- Mantiene intactos V104/V107, 75 frames, 15 landmarks y métricas clínicas.
- Los modelos SKEL privados siguen siendo aportados por el usuario; no se redistribuyen ni se guardan en Supabase.
- BodyExplorer/Z-Anatomy permanece fuera del flujo activo.
