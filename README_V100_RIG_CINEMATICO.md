# V100 · prueba del rig cinemático

1. Mantener **Modo GPU seguro** activado.
2. Abrir la pestaña 11 y esperar a que aparezca `Esqueleto: OK`.
3. Comprobar que el diagnóstico muestra `Rig V100 construido` y recuentos por segmentos.
4. Pulsar **Paso +1** varias veces. El contador debe cambiar `Frame 1/75 → 2/75 → 3/75...` y debe observarse cambio de postura en las extremidades.
5. Si el paso manual funciona, pulsar **Reproducir**. El contador debe avanzar de forma continua.
6. Probar primero sólo con Huesos. La musculatura se carga bajo demanda.

Si el contador avanza pero una región concreta no se mueve, revisar el recuento de mallas asignadas a ese segmento. Si el contador no avanza, el problema está en el reproductor y no en el rig.

V100 mantiene la política de no almacenar los binarios anatómicos en Supabase.
