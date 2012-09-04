#! /usr/bin/env python2

import pygame
from pygame.locals import *
from gamemanager.states import gamestate
from utilidades.imagen import *
from mapa import *
from personaje import *

class PantallaState(gamestate.GameState):
    
    def __init__(self,parent):
        self.parent = parent
        self.background = pygame.Surface(self.parent.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        self.mapa = Mapa('prueba.tmx')
        self.personaje = Personaje('ever','data/imagenes/jugador.png')
        self.personaje.actualizar_posicion((2,37))
        self.mover_personaje = None

    def start(self):
        print "GameState pantalla Started"

    def cleanUp(self):
        print "GameState pantalla Cleaned"
        pass

    def pause(self):
        print "GameState pantalla Paused"
        pass

    def resume(self):
        print "GameState pantalla Resumed"
        pass

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.parent.popState()
                elif event.key == pygame.K_UP:
                    self.mover_personaje = Personaje.NORTE
                elif event.key == pygame.K_DOWN:
                    self.mover_personaje = Personaje.SUR
                elif event.key == pygame.K_RIGHT:
                    self.mover_personaje = Personaje.ESTE
                elif event.key == pygame.K_LEFT:
                    self.mover_personaje = Personaje.OESTE
                    
        k = pygame.key.get_pressed()
        if k[K_UP]: self.mover_personaje = Personaje.NORTE
        elif k[K_DOWN]: self.mover_personaje = Personaje.SUR
        elif k[K_RIGHT]: self.mover_personaje = Personaje.ESTE
        elif k[K_LEFT]: self.mover_personaje = Personaje.OESTE



    def update(self):
        #si se ha intentado mover al personaje
        if (self.mover_personaje != None):
            #comprobamos que la celda donde va a mover es pisable
            if(self.mapa.es_pisable(self.personaje.fila + self.personaje.direcciones[self.mover_personaje][0], self.personaje.columna + self.personaje.direcciones[self.mover_personaje][1])):
                #movemos
                self.personaje.mover(self.mover_personaje)
            else:
                #solo cambiamos direccion
                self.personaje.cambiar_direccion(self.mover_personaje)
            self.mover_personaje = None
        

    def draw(self):
        self.parent.screen.blit(self.background, (0,0))
        self.mapa.dibujar(Mapa.LAYER_SUELO, self.parent.screen,0,0)
        self.mapa.dibujar(Mapa.LAYER_OBJETOS, self.parent.screen,0,0)
        self.mapa.dibujar(Mapa.LAYER_OBJETOS_SUPERPUESTOS, self.parent.screen, 0,0)
        self.personaje.dibujar(self.parent.screen, self.mapa.obtener_centro_celda(self.personaje.fila, self.personaje.columna))
        self.mapa.dibujar(Mapa.LAYER_CIELO, self.parent.screen,0,0)

