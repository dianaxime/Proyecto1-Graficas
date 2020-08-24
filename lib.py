'''
    Diana Ximena de León Figueroa
    Carne 18607
    Proyecto 1 - Escena
    Graficas por Computadora
    22 de agosto de 2020
'''

from obj import Obj
from texture import Texture
import random
import math
from utils import *

'''
    ****************************************
'''
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)

'''
    ****************************************
'''

class Render(object):
    def __init__(self):
        self.framebuffer =[]
        self.zbuffer =[]
        self.color = WHITE
        self.active_vertex_array = []
        self.active_texture = None
        self.active_shader = None
        self.activeNormals = False
        self.customShader = False
        self.isActiveTexture = False
        self.light = V3(0,0,1)

    def createWindow(self, width, height):
        self.width = width
        self.height = height

    def point(self, x, y, selectColor = None):
        try:
            self.framebuffer[y][x] = selectColor or  self.color
        except:
            pass

    def viewport(self, x, y, width, height):
        self.xViewPort = x
        self.yViewPort = y
        self.viewPortWidth = width
        self.viewPortHeight = height

    def clear(self):
        self.framebuffer = [
            [BLACK for x in range(self.width)]
            for y in range(self.height)
        ]

        self.zbuffer = [
            [-float('inf') for x in range(self.width)]
            for y in range(self.height)
        ]

    def clearColor(self, r, g, b):
        newColor = color(r, g, b)
        self.framebuffer = [
            [newColor for x in range(self.width)]
            for y in range(self.height)
        ]

    def setColor(self, r, g, b):
        self.color = color(r, g, b)

    def getCordX(self, x):
        return round((x+1) * (self.viewPortWidth/2) + self.xViewPort)

    def getCordY(self, y):
        return round((y+1) * (self.viewPortHeight/2) + self.yViewPort)

    def vertex(self, x, y):
        self.point(x, y)

    def loadModelMatrix(self, translate, scale, rotate):
        translate = V3(*translate)
        scale = V3(*scale)
        rotate = V3(*rotate)

        translation_matrix = [
            [1, 0, 0, translate.x],
            [0, 1, 0, translate.y],
            [0, 0, 1, translate.z],
            [0, 0, 0, 1],
        ]

        a = rotate.x
        rotation_matrix_x = [
            [1, 0, 0, 0],
            [0, math.cos(a), -math.sin(a), 0],
            [0, math.sin(a),  math.cos(a), 0],
            [0, 0, 0, 1]
        ]

        a = rotate.y
        rotation_matrix_y = [
            [math.cos(a), 0,  math.sin(a), 0],
            [     0, 1,       0, 0],
            [-math.sin(a), 0,  math.cos(a), 0],
            [     0, 0,       0, 1]
        ]

        a = rotate.z
        rotation_matrix_z = [
            [math.cos(a), -math.sin(a), 0, 0],
            [math.sin(a),  math.cos(a), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

        rotation_matrix = MM(rotation_matrix_x, rotation_matrix_y)
        rotation_matrix = MM(rotation_matrix, rotation_matrix_z)

        scale_matrix = [
            [scale.x, 0, 0, 0],
            [0, scale.y, 0, 0],
            [0, 0, scale.z, 0],
            [0, 0, 0, 1],
        ]
        
        result_matrix = MM(translation_matrix, rotation_matrix)
        result_matrix = MM(result_matrix, scale_matrix)
        self.Model = result_matrix
        
    def loadViewMatrix(self, x, y, z, center):
        M = [
            [x.x, x.y, x.z, 0],
            [y.x, y.y, y.z, 0],
            [z.x, z.y, z.z, 0],
            [0,0,0,1]
        ]

        O = [
            [1, 0, 0, -center.x],
            [0, 1, 0, -center.y],
            [0, 0, 1, -center.z],
            [0, 0, 0, 1]
        ]

        self.View = MM(M, O)

    def loadProjectionMatrix(self, coeff):
        self.Projection = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, coeff, 1]
        ]
    
    def loadViewportMatrix(self, x = 0, y = 0):
        self.Viewport = [
            [self.width/2, 0, 0, x + self.width/2],
            [0, self.height/2, 0, y + self.height/2],
            [0, 0, 128, 128],
            [0, 0, 0, 1]
        ]

    def lookAt(self, eye, center, up):
        z = norm(sub(eye, center))
        x = norm(cross(up, z))
        y = norm(cross(z, x))
        self.loadViewMatrix(x, y, z, center)
        self.loadProjectionMatrix(-1 / length(sub(eye, center)))
        self.loadViewportMatrix()

    def line(self, x0, y0, x1, y1):
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        threshold = dx
        y = y0
        inc = 1 if y1 > y0 else -1

        for x in range(x0, x1):
            if steep:
                self.point(y, x)
                
            else:
                self.point(x, y)
                
            offset += 2 * dy
            if offset >= threshold:
                y += inc
                threshold += 2 * dx

    def write(self, filename = 'out.bmp'):
        f = open(filename, 'bw')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()


    def modelLines(self):
        A = next(self.active_vertex_array)
        B = next(self.active_vertex_array)
        self.line(round(A.x), round(A.y), round(B.x), round(B.y))

    def triangleColor(self, selectColor):
        A = next(self.active_vertex_array)
        B = next(self.active_vertex_array)
        C = next(self.active_vertex_array)

        #print(A, B, C)

        if self.activeNormals:
            nA = next(self.active_vertex_array)
            nB = next(self.active_vertex_array)
            nC = next(self.active_vertex_array)

        xMin, xMax, yMin, yMax = bbox(A, B, C)
        for x in range(xMin, xMax + 1):
            for y in range(yMin, yMax + 1):
                P = V2(x, y)
                w, v, u = barycentric(A, B, C, P)
                if w < 0 or v < 0 or u < 0:
                    continue
                
                z = A.z * w + B.z * u + C.z * v

                if self.activeNormals:
                    selectColor = self.gourad(
                        bar = (w, v, u),
                        varying_normals = (nA, nB, nC),
                        tcolor = selectColor
                    )
                
                if x < self.width and y < self.height and z > self.zbuffer[y][x]:
                    self.point(x, y, selectColor)
                    self.zbuffer[y][x] = z
                

    def triangleTexture(self):
        A = next(self.active_vertex_array)
        B = next(self.active_vertex_array)
        C = next(self.active_vertex_array)

        print("v",A, B, C)
        
        if self.isActiveTexture:
            tA = next(self.active_vertex_array)
            tB = next(self.active_vertex_array)
            tC = next(self.active_vertex_array)

        print("t",tA, tB, tC)

        if self.activeNormals:
            nA = next(self.active_vertex_array)
            nB = next(self.active_vertex_array)
            nC = next(self.active_vertex_array)

        print("n",nA, nB, nC)

        xmin, xmax, ymin, ymax = bbox(A, B, C)

        normal = norm(cross(sub(B, A), sub(C, A)))
        intensity = dot(normal, self.light)
        if intensity < 0:
            return

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                w, v, u = barycentric(A, B, C, V2(x, y))
                if w < 0 or v < 0 or u < 0:  
                    continue

                if self.isActiveTexture:
                    tx = tA.x * w + tB.x * u + tC.x * v
                    ty = tA.y * w + tB.y * u + tC.y * v

                    selectColor = self.gourad(
                        bar = (w, v, u),
                        texture_coords = (tx, ty),
                        varying_normals = (nA, nB, nC),
                        tcolor = WHITE
                    )

                if self.customShader:
                    selectColor = self.active_shader(
                        self,
                        triangle = (A, B, C),
                        bar = (w, v, u),
                        varying_normals = (nA, nB, nC)
                    )


                z = A.z * w + B.z * u + C.z * v

                if x < 0 or y < 0:
                    continue

                if x < self.width and y < self.height and z > self.zbuffer[y][x]:
                    self.point(x, y, selectColor)
                    self.zbuffer[y][x] = z


    def transform(self, vertex):
        augmented_vertex = [
            [vertex.x],
            [vertex.y],
            [vertex.z],
            [1]
        ]

        transformed_vertex = MM(self.Projection, self.Viewport)
        transformed_vertex = MM(transformed_vertex, self.View) 
        transformed_vertex = MM(transformed_vertex, self.Model)
        transformed_vertex = MM(transformed_vertex, augmented_vertex)
        
        transformed_vertex = [
            transformed_vertex[0][0],
            transformed_vertex[1][0],
            transformed_vertex[2][0]
        ]
        
        return V3(*transformed_vertex)


    def load(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
        self.loadModelMatrix(translate, scale, rotate)
        model = Obj(filename)
        vertex_buffer_object = []
    
        for face in model.faces:
            for facepart in face:
                vertex = self.transform(V3(*model.vertices[facepart[0]-1]))
                vertex_buffer_object.append(vertex)

            if self.isActiveTexture:
                for facepart in face:
                    if len(model.tvertices[facepart[1]-1]) == 2:
                        tvertex = V2(*model.tvertices[facepart[1]-1])
                    elif len(model.tvertices[facepart[1]-1]) == 3:
                        tvertex = V3(*model.tvertices[facepart[1]-1])
                    vertex_buffer_object.append(tvertex)

            if self.activeNormals:
                for facepart in face:
                    nvertex = V3(*model.normals[facepart[2]-1])
                    vertex_buffer_object.append(nvertex)

        self.active_vertex_array = iter(vertex_buffer_object)

    def gourad(self, **kwargs):
        # barycentric
        w, v, u = kwargs['bar']
        
        tcolor = kwargs['tcolor']
        # texture
        if self.isActiveTexture:
            tx, ty = kwargs['texture_coords']
            tcolor = self.active_texture.get_color(tx, ty)
            print(tx, ty)
        # normals
        nA, nB, nC = kwargs['varying_normals']

        # light intensity
        iA, iB, iC = [dot(n, self.light) for n in (nA, nB, nC)]
        intensity = w * iA + u * iB + v * iC
        return color(
            int(tcolor[2] * intensity) if (tcolor[0] * intensity > 0 and tcolor[0] * intensity < 255) else 0,
            int(tcolor[1] * intensity) if (tcolor[1] * intensity > 0 and tcolor[1] * intensity < 255) else 0,
            int(tcolor[0] * intensity) if (tcolor[2] * intensity > 0 and tcolor[2] * intensity < 255) else 0
        )

    def gradient(self, **kwargs):
        # barycentric
        w, v, u = kwargs['bar']
        # colors
        color1 = kwargs['color1']
        color2 = kwargs['color2']
        color3 = kwargs['color3']

        pColorR = round(color1[0] * w + color1[1] * u + color1[2] * v)
        pColorG = round(color2[0] * w + color2[1] * u + color2[2] * v)
        pColorB = round(color3[0] * w + color3[1] * u + color3[2] * v)

        return color(pColorR, pColorG, pColorB)


    def draw_arrays(self, polygon):
        if polygon == 'TEXTURE':
            try:
                self.isActiveTexture = True
                self.activeNormals = True
                while True:
                    self.triangleTexture()
            except StopIteration:
                self.isActiveTexture = False
                self.activeNormals = False
                print('Done model with texture.')
        elif polygon == 'LINES':
            try:
                while True:
                    self.modelLines()
            except StopIteration:
                print('Done model only with lines.')
        elif polygon == 'COLORS':
            self.activeNormals = True
            try:
                while True:
                    self.triangleColor(
                        color(
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255)
                        )
                    )
            except StopIteration:
                self.activeNormals = False
                print('Done model with random colors.')
        elif polygon == 'FLAT':
            try:
                self.activeNormals = True
                while True:
                    self.triangleColor(
                        color(255, 255, 255)
                    )
            except StopIteration:
                self.activeNormals = False
                print('Done model with flat shading.')
        elif polygon == 'CUSTOM':
            try:
                self.customShader = True
                self.activeNormals = True
                while True:
                    self.triangleTexture()
            except StopIteration:
                self.customShader = False
                self.activeNormals = False
                print('Done model with custom shader.')


def fragment(render, **kwargs):
    # barycentric
    w, v, u = kwargs['bar']
    # coords
    A, B, C = kwargs['triangle']

    t = A.x * w + B.x * u + C.x * v
    grey = int(t * 256)
    if grey < 0:
        grey=0
    if grey > 255:
        grey=255
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

    return color(
        int(tcolor[2] * intensity) if tcolor[0] * intensity > 0 and tcolor[0] * intensity < 255 else 0,
        int(tcolor[1] * intensity) if tcolor[1] * intensity > 0 and tcolor[1] * intensity < 255 else 0,
        int(tcolor[0] * intensity) if tcolor[2] * intensity > 0 and tcolor[2] * intensity < 255 else 0
    )

r = Render()
r.createWindow(1024, 1024)
r.clear()
t = Texture('model.bmp')
r.active_texture = t
r.active_shader = fragment
r.activeNormals = True
r.isActiveTexture = True
#r.draw_arrays('LINES')
#r.lookAt(V3(0, 0, 30), V3(0, 0, 0), V3(5, 5, 5))

r.lookAt(V3(1, 0, 5), V3(0, 0, 0), V3(0, 1, 0))
r.load('model.obj', V3(0, 0, 0), V3(1, 1, 1), V3(0, 0, 0))

'''t = Texture('texture.bmp')
r.lookAt(V3(0, 0, 10), V3(0, 0, -100), V3(0, 1, 0))

r.load('fox.obj', V3(0, 0, 0), V3(1, 1, 1), rotate=(0, 1, 0))
'''
r.draw_arrays('TEXTURE')

r.write()