# -*- coding: utf-8 -*-

import pygame 
from pygame.locals import *

from mapa import *
from personaje import *

class Mundo:
    '''
    Clase para controlar todo lo que ocurre dentro del juego:
    Colisiones, dibujar personajes, control del jugador, etc..
    '''

    def __init__(self, mapa, personajes):
        '''
        Constructor de la clase que obtiene el mapa y los personajes
        que intervendran en esta pantalla
        '''
        self.personajes = personajes #array de los personajes del mundo
        self.jugador = personajes[0] # el primero es el player
        self.mapa = mapa
        self.direccion_movimiento_jugador = None # hacia donde se mueve
        
    def dibujar(self, surface):
        '''
        Dibuja las capas del mapa y TODOS los personajes del juego
        '''
        self.mapa.dibujar(Mapa.LAYER_SUELO, surface,0,0)
        self.mapa.dibujar(Mapa.LAYER_OBJETOS, surface,0,0)
        self.mapa.dibujar(Mapa.LAYER_OBJETOS_SUPERPUESTOS,surface,0,0)

        #Dibujamos los personajes
        for personaje in self.personajes:
            personaje.dibujar(surface, self.mapa.obtener_centro_celda(personaje.fila, personaje.columna))
        self.mapa.dibujar(Mapa.LAYER_CIELO, surface,0,0)

    def update(self):
        '''
        Mueve y actualiza las posiciones de los personajes
        '''
        #si se ha intentado mover al personaje
        if(self.direccion_movimiento_jugador != None ):
            #Calculamos donde va a mover el jugador
            posicion_a_mover = (self.jugador.fila + self.jugador.direcciones[self.direccion_movimiento_jugador][0], self.jugador.columna + self.jugador.direcciones[self.direccion_movimiento_jugador][1])
            
            if ( not self.hay_colision(self.jugador,posicion_a_mover)):
                self.jugador.mover(self.direccion_movimiento_jugador)
            else:
                #solo cambiamos las direccion pero sin moverlo
                self.jugador.cambiar_direccion(self.direccion_movimiento_jugador)
                
            self.direccion_movimiento_jugador = None

            #Ordenamos los personajes por fila, para luego dibujarlos
            self.personajes.sort(self.comparar_posicion_personajes)

    def mover_jugador(self, direccion):
        '''Establece hacia donde debe mover el jugador '''
        self.direccion_movimiento_jugador = direccion

    def hay_colision(self, personaje, destino):
        '''Comprueba la solicion de un personaje u otros'''
        hay_colision = False
        #Comprobamos que la celda donde va a mover es pisable
        if (not self.mapa.es_pisable(destino[0],destino[1])):
            hay_colision = True
            
        #Comprobamos las colisiones con el resto de personajes
        for item in self.personajes:
            if ( item.nombre != personaje.nombre):
                if ( item.obtener_posicion() == destino):
                    hay_colision = True
        
        return hay_colision

    def comparar_posicion_personajes(self,a,b):
        '''Compara y la posicion de un personaje con respecto a su fila '''
        return cmp(int(a.fila), int(b.fila))
