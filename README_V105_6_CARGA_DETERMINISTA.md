# V105.6 · carga/render determinista

Objetivo: impedir que la pestaña quede indefinidamente en `Cargando atlas…`.

El Rig se presenta de forma independiente antes de cualquier importación de Three.js. El atlas óseo se prepara en segundo plano y muestra cada etapa de forma explícita. Los modos Huesos y Rig + Huesos sólo se habilitan cuando el GLB ha sido descargado, clasificado y renderizado al menos una vez. Si la carga falla, el Rig sigue funcionando y el usuario puede pulsar `Reintentar atlas`.

La grabación descargable sigue disponible. Para Rig se captura el canvas independiente; para Huesos y Rig + Huesos se captura el canvas WebGL.
