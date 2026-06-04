import cv2
import numpy as np
import os

ruta_base = os.path.dirname(os.path.abspath(__file__))
ruta_img = os.path.join(ruta_base, "img")
ruta_resultados = os.path.join(ruta_base, "resultados")

if not os.path.exists(ruta_resultados):
    os.makedirs(ruta_resultados)


def cargar_imagen(nombre, modo=cv2.IMREAD_COLOR):
    ruta = os.path.join(ruta_img, nombre)
    imagen = cv2.imread(ruta, modo)

    if imagen is None:
        print("No se pudo cargar:", nombre)

    return imagen


def guardar(nombre, imagen):
    ruta = os.path.join(ruta_resultados, nombre)
    cv2.imwrite(ruta, imagen)


# Misión 1: aclarar imagen oscura
def mision_1():
    imagen = cargar_imagen("m1_oscura.png")

    if imagen is None:
        return

    aclarada = cv2.convertScaleAbs(imagen, alpha=4, beta=40)

    guardar("m1_aclarada.png", aclarada)

    cv2.imshow("Mision 1 - Original oscura", imagen)
    cv2.imshow("Mision 1 - Aclarada", aclarada)


# Misión 2: unir dos mitades
def mision_2():
    mitad1 = cargar_imagen("m2_mitad1.png")
    mitad2 = cargar_imagen("m2_mitad2.png")

    if mitad1 is None or mitad2 is None:
        return

    alto = min(mitad1.shape[0], mitad2.shape[0])

    mitad1 = cv2.resize(mitad1, (mitad1.shape[1], alto))
    mitad2 = cv2.resize(mitad2, (mitad2.shape[1], alto))

    unida = np.hstack((mitad1, mitad2))

    guardar("m2_imagen_unida.png", unida)

    cv2.imshow("Mision 2 - Imagen unida", unida)


# Misión 4: reducir ruido
def mision_4():
    imagen = cargar_imagen("m4_ruido.png")

    if imagen is None:
        return

    sin_ruido = cv2.medianBlur(imagen, 5)

    guardar("m4_sin_ruido.png", sin_ruido)

    cv2.imshow("Mision 4 - Con ruido", imagen)
    cv2.imshow("Mision 4 - Sin ruido", sin_ruido)


# Misión 5: separar canales de color
def mision_5():
    imagen = cargar_imagen("m5_tricolor.png")

    if imagen is None:
        return

    b, g, r = cv2.split(imagen)

    guardar("m5_canal_azul.png", b)
    guardar("m5_canal_verde.png", g)
    guardar("m5_canal_rojo.png", r)

    cv2.imshow("Mision 5 - Canal azul", b)
    cv2.imshow("Mision 5 - Canal verde", g)
    cv2.imshow("Mision 5 - Canal rojo", r)


# Microfilm: mejorar contraste para intentar revelar texto
def microfilm():
    imagen = cargar_imagen("microfilm.jpg", cv2.IMREAD_GRAYSCALE)

    if imagen is None:
        return

    mejorada = cv2.equalizeHist(imagen)
    mejorada = cv2.convertScaleAbs(mejorada, alpha=2, beta=20)

    guardar("microfilm_mejorado.png", mejorada)

    cv2.imshow("Microfilm original", imagen)
    cv2.imshow("Microfilm mejorado", mejorada)


# QR rotado: corregir rotación aproximada
def qr_rotado():
    imagen = cargar_imagen("qr_rotado.jpg")

    if imagen is None:
        return

    alto, ancho = imagen.shape[:2]
    centro = (ancho // 2, alto // 2)

    matriz = cv2.getRotationMatrix2D(centro, 45, 1.0)
    corregida = cv2.warpAffine(imagen, matriz, (ancho, alto))

    guardar("qr_corregido.png", corregida)

    cv2.imshow("QR rotado", imagen)
    cv2.imshow("QR corregido", corregida)


# Vehículo: convertir a gris y detectar bordes
def vehiculo():
    imagen = cargar_imagen("vehiculo.jpg")

    if imagen is None:
        return

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(gris, 100, 200)

    guardar("vehiculo_gris.png", gris)
    guardar("vehiculo_bordes.png", bordes)

    cv2.imshow("Vehiculo original", imagen)
    cv2.imshow("Vehiculo bordes", bordes)


print("Ejecutando misiones de imagen...")

mision_1()
mision_2()
mision_4()
mision_5()
microfilm()
qr_rotado()
vehiculo()

print("Proceso terminado. Revisa la carpeta resultados.")

cv2.waitKey(0)
cv2.destroyAllWindows()