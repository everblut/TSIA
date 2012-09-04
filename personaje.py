
from pygame.locals import *

from utilidades.imagen import *

class Personaje():
    TILE_ALTO = 32
    TILE_ANCHO = 32

    NORTE = 0
    SUR = 1
    ESTE = 2
    OESTE = 3

    def __init__(self,nombre,imagen):
        #nombre del pj
        self.nombre = nombre

        #tileset con la animacion del personaje
        self.tileset = cortar_tileset(imagen, (Personaje.TILE_ANCHO, Personaje.TILE_ALTO), False)
        
        self.direccion = Personaje.SUR
        self.direcciones = [[-1,0], [+1,0], [0, +1], [0, -1]]
        #N,S,E,O

        #dibujar el personaje
        self.offset = (16,28)

        #Fila y columna donde esta el personaje 
        self.fila = 0
        self.columna = 0

        self.animacion = [[0], [5], [1], [6]]

    def update(self):
        pass

    def dibujar(self, destino, coordenadas):
        cuadro_animacion = self.animacion[self.direccion][0]
        destino.blit(self.tileset[cuadro_animacion], (coordenadas[0] - self.offset[0], coordenadas[1] - self.offset[1]))
        
    def actualizar_posicion(self,(fila,columna)):
        self.fila = fila
        self.columna = columna

    def mover(self, orientacion):
        self.direccion = orientacion
        self.fila += self.direcciones[self.direccion][0]
        self.columna += self.direcciones[self.direccion][1]

    def cambiar_direccion(self, direccion):
        self.direccion = direccion
