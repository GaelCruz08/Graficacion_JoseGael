# Segmentación de Frutas usando HSV

## Descripción

En esta práctica se trabaja con una imagen de frutas para aplicar segmentación por color usando el modelo HSV.

El programa convierte la imagen original a HSV y genera máscaras binarias para detectar frutas de diferentes colores, principalmente rojo, verde y amarillo.

## Objetivo

Aplicar el modelo de color HSV para segmentar objetos por color y analizar los resultados mediante máscaras binarias.

## Archivos

- `frutas.png`: imagen original utilizada en la práctica.
- `segmentacion_hsv.py`: código principal de la práctica.
- `resultados/`: carpeta generada automáticamente con las máscaras obtenidas.

## Colores analizados

- Rojo
- Verde
- Amarillo

## Proceso realizado

1. Se carga la imagen original.
2. Se convierte la imagen de BGR a HSV.
3. Se crean rangos de color para rojo, verde y amarillo.
4. Se generan máscaras binarias.
5. Se aplica limpieza de ruido con operaciones morfológicas.
6. Se cuentan las regiones conectadas detectadas.
7. Se guardan los resultados en una carpeta.

## Conclusión

El modelo HSV facilita la segmentación por color porque separa el tono, la saturación y el valor de iluminación. Esto permite detectar objetos de un color específico de forma más clara que usando directamente RGB.