'''
    Diana Ximena de León Figueroa
    Carne 18607
    Proyecto 1 - Escena
    Graficas por Computadora
    22 de agosto de 2020
'''

from lib import Render
from texture import Texture
from utils import V2, V3

bitmap = Render()


def glInit():
    pass


def glCreateWindow(width, height):
    bitmap.createWindow(width, height)


def glViewport(x, y, width, height):
    bitmap.viewport(x, y, width, height)


def glClear():
    bitmap.clear()


def glClearColor(r, g, b):
    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)
    bitmap.clearColor(r, g, b)


def glColor(r, g, b):
    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)
    bitmap.setColor(r, g, b)


def glVertex(x, y):
    X = bitmap.getCordX(x)
    Y = bitmap.getCordY(y)
    bitmap.vertex(X, Y)


def glPoint(x, y):
    X = bitmap.getCordX(x)
    Y = bitmap.getCordY(y)
    bitmap.point(X, Y)


def glLine(x0, y0, x1, y1):
    x0 = bitmap.getCordX(x0)
    y0 = bitmap.getCordY(y0)
    x1 = bitmap.getCordX(x1)
    y1 = bitmap.getCordY(y1)
    bitmap.line(x0, y0, x1, y1)


def glLoad(filename, translate, scale, rotate):
    bitmap.load(filename, translate, scale, rotate)


def glDrawFigure(figure):
    bitmap.draw_arrays(figure)


def glLookAt(eye, center, up):
    bitmap.lookAt(eye, center, up)


def glIsActiveTexture(boolean):
    bitmap.isActiveTexture = boolean


def glIsActiveNormals(boolean):
    bitmap.activeNormals = boolean


def glIsActiveShader(boolean):
    bitmap.customShader = boolean


def glChangeTexture(filename):
    t = Texture(filename)
    bitmap.active_texture = t


def glChangeShader(shader):
    bitmap.active_shader = shader


def glChangeLight(light):
    bitmap.light = light


def glFinish(filename='out.bmp'):
    bitmap.write(filename)


glCreateWindow(1000, 1000)
glClear()
glIsActiveNormals(True)
glIsActiveTexture(True)
glChangeTexture('texture.bmp')
glLookAt(V3(0, 0, 10), V3(0, 0, -100), V3(0, 1, 0))
glLoad('fox.obj', V3(0, 0, 0), V3(0.01, 0.01, 0.01), rotate=(0, 1, 0))
glDrawFigure('TEXTURE')
glFinish()
