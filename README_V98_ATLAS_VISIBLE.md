# V98 · Atlas anatómico real visible

V98 corrige específicamente el problema observado en V97: los GLB se cargaban (201 mallas de esqueleto + 467 de musculatura) pero el lienzo permanecía vacío.

El visor ahora carga los GLB, mide el `Box3` en coordenadas originales, centra el contenido dentro de un nodo que después se escala, adapta automáticamente la cámara y los planos de clipping, muestra primero una pose estática comprobable y sólo después permite reproducir la cinemática biplanar.

Si el atlas se ve correctamente, el HUD mostrará `Atlas visible: SÍ` junto con tamaño, centro, escala y distancia de cámara.
