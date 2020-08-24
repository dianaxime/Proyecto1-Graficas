'''
    Diana Ximena de León Figueroa
    Carne 18607
    Proyecto 1 - Escena
    Graficas por Computadora
    22 de agosto de 2020
'''
import struct


def color(r, g, b):
    return bytes([b, g, r])


'''
Cargar una Textura de una imagen .bmp 
Para convertir de .PNG, .JPG a .bmp:
    https://imagen.online-convert.com/es/convertir-a-bmp
'''


class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        image = open(self.path, "rb")
        image.seek(2 + 4 + 4)
        header_size = struct.unpack("=l", image.read(4))[0]  
        image.seek(2 + 4 + 4 + 4 + 4)
        self.width = struct.unpack("=l", image.read(4))[0]  
        self.height = struct.unpack("=l", image.read(4))[0]
        self.pixels = []
        image.seek(header_size)
        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1))
                g = ord(image.read(1))
                r = ord(image.read(1))
                self.pixels[y].append(color(r, g, b))
        image.close()

    def get_color(self, tx, ty, intensity=1):
        x = int(tx * self.width)
        y = int(ty * self.height)
        #x=int(tx)
        #y=int(ty)
        try:
            return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.pixels[y][x]))
        except:
            pass
