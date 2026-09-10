# V105.2 · Hotfix JavaScript del atlas óseo

Esta versión corrige el bloqueo de V105.1 en el que el visor permanecía en «Cargando atlas…». La causa era un error de sintaxis JavaScript en el HTML generado: ciertas secuencias `\n` del código fuente Python se convertían en saltos de línea reales dentro de cadenas JavaScript. V105.2 las escapa correctamente y además carga Three.js/OrbitControls/GLTFLoader mediante `import()` dinámico con diagnóstico visible.

Secuencia esperada en pantalla:

1. `Motor 3D iniciado · cargando librerías…`
2. `Motor 3D OK · preparando atlas…`
3. `Cargando atlas óseo… GitHub raw` o fallback `jsDelivr`
4. `Atlas descargado · clasificando ... mallas…`
5. `Atlas OK · ... mallas · ... frames`

Si falla una etapa, el motivo queda mostrado en el propio panel.
