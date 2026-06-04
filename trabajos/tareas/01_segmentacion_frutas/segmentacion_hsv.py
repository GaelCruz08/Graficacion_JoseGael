import cv2
import numpy as np
import os

# Crear carpeta para guardar los resultados
if not os.path.exists("resultados"):
    os.makedirs("resultados")

# Leer la imagen original
imagen = cv2.imread("frutas.png")

if imagen is None:
    print("No se pudo cargar la imagen frutas.png")
    exit()

# Convertir imagen de BGR a HSV
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Rangos para detectar colores
# Rojo se divide en dos rangos porque en HSV está al inicio y al final
rojo_bajo1 = np.array([0, 80, 80])
rojo_alto1 = np.array([10, 255, 255])

rojo_bajo2 = np.array([170, 80, 80])
rojo_alto2 = np.array([180, 255, 255])

verde_bajo = np.array([35, 60, 60])
verde_alto = np.array([85, 255, 255])

amarillo_bajo = np.array([20, 80, 80])
amarillo_alto = np.array([35, 255, 255])

# Crear máscaras
mascara_rojo1 = cv2.inRange(hsv, rojo_bajo1, rojo_alto1)
mascara_rojo2 = cv2.inRange(hsv, rojo_bajo2, rojo_alto2)
mascara_rojo = cv2.bitwise_or(mascara_rojo1, mascara_rojo2)

mascara_verde = cv2.inRange(hsv, verde_bajo, verde_alto)
mascara_amarillo = cv2.inRange(hsv, amarillo_bajo, amarillo_alto)

# Limpieza de ruido con operación morfológica
kernel = np.ones((5, 5), np.uint8)

rojo_limpio = cv2.morphologyEx(mascara_rojo, cv2.MORPH_OPEN, kernel)
verde_limpio = cv2.morphologyEx(mascara_verde, cv2.MORPH_OPEN, kernel)
amarillo_limpio = cv2.morphologyEx(mascara_amarillo, cv2.MORPH_OPEN, kernel)

# Función para contar regiones conectadas
def contar_regiones(mascara, nombre):
    total, etiquetas, estadisticas, centroides = cv2.connectedComponentsWithStats(mascara)

    contador = 0
    areas = []

    for i in range(1, total):
        area = estadisticas[i, cv2.CC_STAT_AREA]

        if area > 300:
            contador += 1
            areas.append(area)

    print("Color:", nombre)
    print("Frutas detectadas:", contador)
    print("Areas aproximadas:", areas)
    print("-----------------------------")

# Conteo por color
contar_regiones(rojo_limpio, "Rojo")
contar_regiones(verde_limpio, "Verde")
contar_regiones(amarillo_limpio, "Amarillo")

# Guardar resultados
cv2.imwrite("resultados/imagen_original.png", imagen)
cv2.imwrite("resultados/imagen_hsv.png", hsv)
cv2.imwrite("resultados/mascara_rojo.png", mascara_rojo)
cv2.imwrite("resultados/mascara_rojo_limpia.png", rojo_limpio)
cv2.imwrite("resultados/mascara_verde.png", mascara_verde)
cv2.imwrite("resultados/mascara_verde_limpia.png", verde_limpio)
cv2.imwrite("resultados/mascara_amarillo.png", mascara_amarillo)
cv2.imwrite("resultados/mascara_amarillo_limpia.png", amarillo_limpio)

# Mostrar ventanas
cv2.imshow("Imagen original", imagen)
cv2.imshow("Mascara rojo limpia", rojo_limpio)
cv2.imshow("Mascara verde limpia", verde_limpio)
cv2.imshow("Mascara amarillo limpia", amarillo_limpio)

cv2.waitKey(0)
cv2.destroyAllWindows()