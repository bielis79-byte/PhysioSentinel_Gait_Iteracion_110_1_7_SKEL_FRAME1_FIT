# PhysioSentinel Gait · V110.1.2

Hotfix de resolución de dependencias para Streamlit Cloud.

- Corrige el conflicto demostrado en el log entre `numpy>=2.1` y `moderngl-window==2.4.6`, que exige `numpy<2`.
- Fija NumPy a `>=1.26,<2`, compatible con Streamlit 1.63 y con la rama SKEL/moderngl-window.
- Mantiene SKEL fijado al commit validado por el despliegue anterior.
- Mantiene el OpenCV 5 headless aislado de V86.6 con `--no-deps`, por lo que este cambio no altera su instalación aislada.
- No reincorpora BodyExplorer/Z-Anatomy.
- No modifica V104/V107, los 75 frames ni las métricas clínicas.
- Los modelos SKEL privados `.pkl` siguen siendo aportados por el usuario y no se redistribuyen.
