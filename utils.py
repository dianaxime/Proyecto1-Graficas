'''
    Diana Ximena de León Figueroa
    Carne 18607
    Proyecto 1 - Escena
    Graficas por Computadora
    22 de agosto de 2020
'''

from collections import namedtuple
import struct

V2 = namedtuple('Vertex2', ['x', 'y'])
V3 = namedtuple('Vertex3', ['x', 'y', 'z'])

'''
Multiplicacion de Matrices 
Extraido de:
    https://www.it-swarm.dev/es/python/python-3-multiplicar-un-vector-por-una-matriz-sin-numpy/1051381438/
'''


def MM(a, b):
    c = []
    for i in range(0, len(a)):
        temp = []
        for j in range(0, len(b[0])):
            s = 0
            for k in range(0, len(a[0])):
                s += a[i][k]*b[k][j]
            temp.append(s)
        c.append(temp)
    return c


'''
***********************************************************************************************************
PROPORCIONADAS POR DENNIS
***********************************************************************************************************
'''


def char(c):
    return struct.pack('=c', c.encode('ascii'))


def word(c):
    return struct.pack('=h', c)


def dword(c):
    return struct.pack('=l', c)


def color(r, g, b):
    return bytes([b, g, r])


def sum(v0, v1):
    """
      Input: 2 size 3 vectors
      Output: Size 3 vector with the per element sum
    """
    return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)


def sub(v0, v1):
    """
      Input: 2 size 3 vectors
      Output: Size 3 vector with the per element substraction
    """
    return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)


def mul(v0, k):
    """
      Input: 2 size 3 vectors
      Output: Size 3 vector with the per element multiplication
    """
    return V3(v0.x * k, v0.y * k, v0.z * k)


def dot(v0, v1):
    """
      Input: 2 size 3 vectors
      Output: Scalar with the dot product
    """
    return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z


def length(v0):
    """
      Input: 1 size 3 vector
      Output: Scalar with the length of the vector
    """
    return (v0.x**2 + v0.y**2 + v0.z**2)**0.5


def norm(v0):
    """
      Input: 1 size 3 vector
      Output: Size 3 vector with the normal of the vector
    """
    v0length = length(v0)

    if not v0length:
        return V3(0, 0, 0)

    return V3(v0.x/v0length, v0.y/v0length, v0.z/v0length)


def cross(u, w):
    # print(u, w)
    return V3(
        u.y * w.z - u.z * w.y,
        u.z * w.x - u.x * w.z,
        u.x * w.y - u.y * w.x,
    )


def bbox(*vertices):
    xs = [vertex.x for vertex in vertices]
    ys = [vertex.y for vertex in vertices]
    xs.sort()
    ys.sort()

    xMin = round(xs[0])
    xMax = round(xs[-1])
    yMin = round(ys[0])
    yMax = round(ys[-1])

    return xMin, xMax, yMin, yMax


def barycentric(A, B, C, P):
    cx, cy, cz = cross(
        V3(B.x - A.x, C.x - A.x, A.x - P.x),
        V3(B.y - A.y, C.y - A.y, A.y - P.y)
    )

    if abs(cz) < 1:
        return -1, -1, -1

    u = cx / cz
    v = cy / cz
    w = 1 - (cx + cy) / cz

    return w, v, u
