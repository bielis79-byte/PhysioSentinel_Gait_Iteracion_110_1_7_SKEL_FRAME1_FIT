# PhysioSentinel Gait · V110.1

- Retirada completa del flujo activo de la pestaña 3D de BodyExplorer/Z-Anatomy/V108.x.
- Se conserva intacta la cinemática V104/V107 y el puente de 15 landmarks validado en V109.1/V110.
- Añadido runtime oficial SKEL como dependencia de despliegue, siguiendo el repositorio oficial actualizado para Python 3.12.
- Los modelos privados `skel_male.pkl` / `skel_female.pkl` NO se incluyen ni redistribuyen; siguen entrando mediante ZIP privado del usuario.
- Diagnóstico explícito del import de SKEL y versión de PyTorch.
- No se añade `packages.txt`.
- V110.1 sigue siendo una puerta de validación de UN frame; no anima 75 frames todavía.
