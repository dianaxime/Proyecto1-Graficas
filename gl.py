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


def glCustomClear():
    bitmap.customClearColor()


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
glCustomClear()
#glIsActiveNormals(True)
#glIsActiveTexture(True)
#glChangeTexture('bamboo_shark.bmp')
'''
glLookAt(V3(0, 0, -0.5), V3(0, 0, 0), V3(0, 1, 0))
glLoad('bamboo_shark.obj', V3(0, 0.5, 0), V3(0.001, 0.001, 0.001), rotate=(-0.50, -0.50, 0))
'''
'''
glLookAt(V3(1, 1, 100), V3(0, 0, 0), V3(0, 1, 0))
glLoad('CitizenSnipsV2_1.obj', V3(0, 0, 0), V3(3, 3, 3), rotate=(0, 0, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.9, -1, 0), V3(0.1, 0.1, 0.1), rotate=(0, 0, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-purple.obj', V3(0.8, -0.9, 0), V3(0.25, 0.25, 0.25), rotate=(0.75, 0, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('tuna.obj', V3(0, 0, 0), V3(0.1, 0.1, 0.1), rotate=(0, 0, 0))
'''
'''
no me gusta como se ve :(
glLookAt(V3(0, 1, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('grass-plant.obj', V3(0, -1, 0), V3(0.1, 0.1, 0.1), rotate=(0.2, 0, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral.obj', V3(0, -0.76, 0), V3(0.05, 0.05, 0.05), rotate=(0, 0, -0.2))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish03.obj', V3(-0.2, -0.2, 0), V3(0.0005, 0.0005, 0.0005), rotate=(1, 1, 0))
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('decoration.obj', V3(0, 0, 0), V3(0.01, 0.01, 0.01), rotate=(0, 0, 0))
glDrawFigure('LINES')
glFinish()
