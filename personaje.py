# -*- coding:utf-8 -*-
#            personaje.py
# script provicional para el proyecto TSIA
# variables
#    TILE_ALTO, TILE_ANCHO : constantes size del sprite del personaje
#    NORTE,SUR,ESTE,OESTE  : asignacion numerica para posibles movimientos

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
        '''
           Constructor que recibe un nombre para reconocer al personaje
           ademas recibe la imagen que contiene el sprite del personaje
        '''

        self.nombre = nombre

        #tileset cortador con la imagen del personaje
        self.tileset = cortar_tileset(imagen, (Personaje.TILE_ANCHO, Personaje.TILE_ALTO), False)
        self.direccion = Personaje.SUR
        self.direcciones = [[-1,0], [+1,0], [0, +1], [0, -1]]
        #Direcciones: ( estan al reves las coordenadas ) 
        #Norte = -1 movimiento en Y | Este = +1 movimiento en X
        #Sur = +1 movimiento en Y   | Oeste = -1 movimiento en X

        #size real de cada vista del sprite
        self.offset = (16,28)
        self.fila = 0
        self.columna = 0
        #animaciones elejidas para cuando camina en Norte,Sur,Este y Oeste
        self.animacion = [[0], [5], [1], [6]]

    
    def update(self):
        ''' Futuro uso * '''
        pass

    def dibujar(self, destino, coordenadas):
        '''
        Metodo para dibujar el personaje, utiliza sus coordenadas y el destino del movimiento
        '''
        cuadro_animacion = self.animacion[self.direccion][0]
        destino.blit(self.tileset[cuadro_animacion], (coordenadas[0] - self.offset[0], coordenadas[1] - self.offset[1]))
        
    def actualizar_posicion(self,(fila,columna)):
        #Actualiza la posicion del personaje
        self.fila = fila
        self.columna = columna

    def mover(self, orientacion):
        '''
        Primero verificamos hacia que lado se quiere mover, despues actualizamos la fila y columna nuevas
        '''
        self.direccion = orientacion
        self.fila += self.direcciones[self.direccion][0]
        self.columna += self.direcciones[self.direccion][1]

    def cambiar_direccion(self, direccion):
        #solo cambia el sprite de direccion, dependiendo el movimiento que se realize
        self.direccion = direccion

    def obtener_posicion(self):
        return (self.fila,self.columna)
