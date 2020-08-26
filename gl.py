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
from shaders import fragment, ray

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


'''
glColor(0.37, 0.21, 0.06)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral.obj', V3(-0.4, -0.80, 0), V3(0.04, 0.04, 0.04), rotate=(0, 0, -0.2))
glDrawFigure('LINES')

glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral.obj', V3(0.4, -0.85, 0), V3(0.03, 0.03, 0.03), rotate=(0, 0, -0.2))
glDrawFigure('LINES')

glColor(0.78, 0.73, 0.65)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral.obj', V3(0, -0.76, 0), V3(0.05, 0.05, 0.05), rotate=(0, 0, -0.2))
glDrawFigure('LINES')

glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral.obj', V3(0.8, -0.76, 0), V3(0.05, 0.05, 0.05), rotate=(0, 0, -0.2))
glDrawFigure('LINES')


glColor(0.11, 0.01, 0.02)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('decoration.obj', V3(-1, -1, 0), V3(0.02, 0.02, 0.02), rotate=(0, -0.5, 0))
glDrawFigure('LINES')

glColor(0.52, 0.19, 0.24)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('decoration.obj', V3(-1, -1, 0), V3(0.01, 0.01, 0.01), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.11, 0.01, 0.02)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('decoration.obj', V3(-1, -0.9, 0), V3(0.005, 0.005, 0.005), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.11, 0.01, 0.02)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('decoration.obj', V3(-0.9, -1, 0), V3(0.005, 0.005, 0.005), rotate=(0, 0, 0))
glDrawFigure('LINES')


glColor(0.02, 0.25, 0.26)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-purple.obj', V3(0.8, -0.95, 0), V3(0.25, 0.20, 0.25), rotate=(0.40, 0, 0))
glDrawFigure('LINES')

glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-purple.obj', V3(-0.8, -0.95, 0), V3(0.25, 0.20, 0.25), rotate=(0.40, 0, 0))
glDrawFigure('LINES')

glColor(0.6, 0.49, 0.09)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-purple.obj', V3(0.8, -0.8, 0), V3(0.25, 0.20, 0.25), rotate=(0.40, 0, 0))
glDrawFigure('LINES')

glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-purple.obj', V3(0, -0.8, 0), V3(0.25, 0.20, 0.25), rotate=(0.40, 0, 0))
glDrawFigure('LINES')


glColor(0.26, 0.47, 0.42)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.9, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.77, 0.73, 0.38)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.8, -1, 0), V3(0.5, 0.2, 0.2), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.57, 0.28, 0.16)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.7, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.26, 0.47, 0.42)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.6, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.57, 0.28, 0.16)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.5, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.77, 0.73, 0.38)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.4, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.3, -1, 0), V3(0.5, 0.2, 0.2), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.57, 0.28, 0.16)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.2, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.77, 0.73, 0.38)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(-0.1, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.26, 0.47, 0.42)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(0, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(0.1, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.77, 0.73, 0.38)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(0.2, -1, 0), V3(0.5, 0.2, 0.2), rotate=(0, 0, 0))
glDrawFigure('LINES')

glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(0.3, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.26, 0.47, 0.42)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(0.4, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.57, 0.28, 0.16)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(0.5, -1, 0), V3(0.5, 0.2, 0.2), rotate=(0, 0, 0))
glDrawFigure('LINES')

glColor(0.77, 0.73, 0.38)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('coral-plants.obj', V3(0.6, -1, 0), V3(0.5, 0.1, 0.1), rotate=(0, 0, 0))
glDrawFigure('LINES')

'''


'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('tuna.obj', V3(0, 0, 0), V3(0.1, 0.1, 0.1), rotate=(0, 0, 0))
'''

'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish03.obj', V3(-0.2, -0.2, 0), V3(0.0005, 0.0005, 0.0005), rotate=(1, 1, 0))
'''
#glIsActiveTexture(True)
#glChangeTexture('ray.bmp')

glIsActiveNormals(True)
glIsActiveShader(True)
glChangeShader(ray)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(1, 0, 0))
glLoad('ray.obj', V3(0.5, 0.05, 0), V3(0.003, 0.003, 0.003), rotate=(0, 0, -0.3))
glDrawFigure('CUSTOM')

glIsActiveNormals(False)
glIsActiveShader(False)
glColor(0.09, 0.15, 0.36)
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(1, 0, 0))
glLoad('ray.obj', V3(0.5, 0.05, 0), V3(0.003, 0.003, 0.003), rotate=(0, 0, -0.3))
glDrawFigure('LINES')


'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish01.obj', V3(-0.2, -0.2, 0), V3(0.0005, 0.0005, 0.0005), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish02.obj', V3(-0.2, -0.2, 0), V3(0.0005, 0.0005, 0.0005), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish04.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish05.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish06.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish07.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish08.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish09.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish10.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish11.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish12.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish13.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish14.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''
'''
glLookAt(V3(0, 0, 1), V3(0, 0, 0), V3(0, 1, 0))
glLoad('TropicalFish15.obj', V3(-0.2, -0.2, 0), V3(0.0008, 0.0008, 0.0008), rotate=(1, 1, 0))
'''

'''
glLookAt(V3(0, 0, -0.5), V3(0, 0, 0), V3(0, 1, 0))
glLoad('bamboo_shark.obj', V3(0, 0.5, 0), V3(0.001, 0.001, 0.001), rotate=(-0.50, -0.50, 0))
'''
'''
glLookAt(V3(1, 1, 100), V3(0, 0, 0), V3(0, 1, 0))
glLoad('CitizenSnipsV2_1.obj', V3(0, 0, 0), V3(3, 3, 3), rotate=(0, 0, 0))
'''

glFinish()
