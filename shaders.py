'''
    Diana Ximena de León Figueroa
    Carne 18607
    Proyecto 1 - Escena
    Graficas por Computadora
    22 de agosto de 2020
'''
from utils import color, dot


def fragment(render, **kwargs):
    # barycentric
    w, v, u = kwargs['bar']
    # coords
    A, B, C = kwargs['triangle']

    t = A.x * w + B.x * u + C.x * v
    grey = int(t * 256)
    if grey < 0:
        grey = 0
    if grey > 255:
        grey = 255
    tcolor = color(grey, 100, 100)
    # normals
    nA, nB, nC = kwargs['varying_normals']

    # light intensity
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    intensity = w * iA + u * iB + v * iC

    if (intensity > 0.85):
        intensity = 1
    elif (intensity > 0.60):
        intensity = 0.80
    elif (intensity > 0.45):
        intensity = 0.60
    elif (intensity > 0.30):
        intensity = 0.45
    elif (intensity > 0.15):
        intensity = 0.30
    else:
        intensity = 0

    r = int(tcolor[2] * intensity)
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    g = int(tcolor[1] * intensity)
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    b = int(tcolor[0] * intensity)
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    return color(r, g, b)


def ray(render, **kwargs):
    # barycentric
    w, v, u = kwargs['bar']
    # coords
    A, B, C = kwargs['triangle']

    t = A.x * w + B.x * u + C.x * v
    grey = int(t * 256)
    if grey < 0:
        grey = 0
    if grey > 255:
        grey = 255
    tcolor = color(30, 60, grey)
    # normals
    nA, nB, nC = kwargs['varying_normals']

    # light intensity
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    intensity = w * iA + u * iB + v * iC

    if (intensity > 0.85):
        intensity = 1
    elif (intensity > 0.60):
        intensity = 0.80
    elif (intensity > 0.45):
        intensity = 0.60
    elif (intensity > 0.30):
        intensity = 0.45
    elif (intensity > 0.15):
        intensity = 0.30
    else:
        intensity = 0

    r = int(tcolor[2] * intensity)
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    g = int(tcolor[1] * intensity)
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    b = int(tcolor[0] * intensity)
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    return color(r, g, b)


def shark(render, **kwargs):
    # barycentric
    w, v, u = kwargs['bar']
    # coords
    A, B, C = kwargs['triangle']

    t = A.x * w + B.x * u + C.x * v
    grey = int(t * 256)
    if grey < 0:
        grey = 0
    if grey > 255:
        grey = 255
    tcolor = color(grey, 150, 170)
    # normals
    nA, nB, nC = kwargs['varying_normals']

    # light intensity
    iA, iB, iC = [dot(n, render.light) for n in (nA, nB, nC)]
    intensity = w * iA + u * iB + v * iC

    if (intensity > 0.85):
        intensity = 1
    elif (intensity > 0.60):
        intensity = 0.80
    elif (intensity > 0.45):
        intensity = 0.60
    elif (intensity > 0.30):
        intensity = 0.45
    elif (intensity > 0.15):
        intensity = 0.30
    else:
        intensity = 0

    r = int(tcolor[2] * intensity)
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    g = int(tcolor[1] * intensity)
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    b = int(tcolor[0] * intensity)
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    return color(r, g, b)