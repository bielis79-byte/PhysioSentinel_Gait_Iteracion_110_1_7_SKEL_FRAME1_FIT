# PhysioSentinel Gait · V110.1.3

Hotfix de resolución de dependencias para Streamlit Cloud.

- Restaura `numpy>=2.1,<2.6`, requerido por OpenSim 4.6 a través de Pose2Sim 0.10.49.
- Elimina `moderngl-window==2.4.6` del entorno principal: su restricción `numpy<2` hacía imposible resolver conjuntamente Pose2Sim/OpenSim.
- Mantiene SKEL fijado al commit ya alcanzado por Streamlit, pero se usa como motor matemático/CPU; no se instala su stack de ventana OpenGL para el forward/fitting.
- Mantiene PyTorch, SMPL-X, trimesh y tqdm para el puente SKEL.
- Mantiene intactos V104/V107, los 75 frames, los 15 landmarks y las métricas clínicas.
- Mantiene el OpenCV 5 headless aislado de V86.6.
- No reincorpora BodyExplorer/Z-Anatomy al flujo activo.
- Los modelos SKEL privados `.pkl` no se redistribuyen.
