import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math


def iniciar_ventana():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Primitivas basicas en OpenGL")

    glClearColor(0.08, 0.08, 0.08, 1)
    gluOrtho2D(-10, 10, -7, 7)


def dibujar_ejes():
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_LINES)

    glVertex2f(-10, 0)
    glVertex2f(10, 0)

    glVertex2f(0, -7)
    glVertex2f(0, 7)

    glEnd()


def dibujar_puntos():
    glPointSize(8)
    glColor3f(1, 0, 0)

    glBegin(GL_POINTS)
    glVertex2f(-8, 5)
    glVertex2f(-7, 4)
    glVertex2f(-6, 5)
    glEnd()


def dibujar_lineas():
    glColor3f(0, 1, 0)
    glLineWidth(3)

    glBegin(GL_LINES)
    glVertex2f(-9, 2)
    glVertex2f(-5, 2)

    glVertex2f(-9, 1)
    glVertex2f(-5, 0)
    glEnd()


def dibujar_triangulo():
    glColor3f(0, 0.5, 1)

    glBegin(GL_TRIANGLES)
    glVertex2f(-2, 1)
    glVertex2f(1, 1)
    glVertex2f(-0.5, 4)
    glEnd()


def dibujar_cuadrado():
    glColor3f(1, 1, 0)

    glBegin(GL_QUADS)
    glVertex2f(3, 1)
    glVertex2f(6, 1)
    glVertex2f(6, 4)
    glVertex2f(3, 4)
    glEnd()


def dibujar_circulo():
    glColor3f(1, 0, 1)

    radio = 1.5
    centro_x = -6
    centro_y = -4

    glBegin(GL_POLYGON)

    for i in range(80):
        angulo = 2 * math.pi * i / 80
        x = centro_x + radio * math.cos(angulo)
        y = centro_y + radio * math.sin(angulo)
        glVertex2f(x, y)

    glEnd()


def dibujar_poligono():
    glColor3f(0, 1, 1)

    glBegin(GL_POLYGON)
    glVertex2f(2, -5)
    glVertex2f(5, -5)
    glVertex2f(6, -3)
    glVertex2f(4, -1)
    glVertex2f(2, -2)
    glEnd()


def dibujar_escena():
    glClear(GL_COLOR_BUFFER_BIT)

    dibujar_ejes()
    dibujar_puntos()
    dibujar_lineas()
    dibujar_triangulo()
    dibujar_cuadrado()
    dibujar_circulo()
    dibujar_poligono()

    pygame.display.flip()


def main():
    iniciar_ventana()

    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                ejecutando = False

        dibujar_escena()

    pygame.quit()


if __name__ == "__main__":
    main()