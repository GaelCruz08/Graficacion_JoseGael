import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


angulo = 0
escala = 1
direccion_escala = 1


def iniciar_ventana():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Transformaciones geometricas")

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


def dibujar_cuadrado():
    glBegin(GL_QUADS)

    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glVertex2f(1, 1)
    glVertex2f(-1, 1)

    glEnd()


def cuadrado_normal():
    glPushMatrix()

    glColor3f(0, 0.7, 1)
    glTranslatef(-6, 0, 0)
    dibujar_cuadrado()

    glPopMatrix()


def cuadrado_trasladado():
    glPushMatrix()

    glColor3f(0, 1, 0)
    glTranslatef(-2, 2, 0)
    dibujar_cuadrado()

    glPopMatrix()


def cuadrado_rotado():
    glPushMatrix()

    glColor3f(1, 0.5, 0)
    glTranslatef(2, 0, 0)
    glRotatef(angulo, 0, 0, 1)
    dibujar_cuadrado()

    glPopMatrix()


def cuadrado_escalado():
    glPushMatrix()

    glColor3f(1, 0, 1)
    glTranslatef(6, 0, 0)
    glScalef(escala, escala, 1)
    dibujar_cuadrado()

    glPopMatrix()


def dibujar_escena():
    glClear(GL_COLOR_BUFFER_BIT)

    dibujar_ejes()
    cuadrado_normal()
    cuadrado_trasladado()
    cuadrado_rotado()
    cuadrado_escalado()

    pygame.display.flip()


def main():
    global angulo, escala, direccion_escala

    iniciar_ventana()

    reloj = pygame.time.Clock()
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                ejecutando = False

        angulo += 1

        escala += 0.01 * direccion_escala

        if escala >= 1.8:
            direccion_escala = -1

        if escala <= 0.6:
            direccion_escala = 1

        dibujar_escena()
        reloj.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
    