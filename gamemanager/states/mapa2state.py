# -*- coding: utf-8 -*-
#
# En la tecla ESC, te hace un pop al state pasado... se necesita volver al menu, pero del menu volver a este propio state
#

import pygame
from pygame.locals import *
from gamemanager.states import gamestate
from utilidades.imagen import *

from mapa import *
from personaje import *
from mundo import *
import menustate
import mapa1state

class Mapa2State(gamestate.GameState):

    def __init__(self,parent):
        self.parent = parent
        self.mapa = Mapa('prueba1.tmx')
        self.ordenador = Personaje('ordenador1','data/imagenes/policia.png')
        self.ordenador.actualizar_posicion((20,29))
        self.parent.jugador.actualizar_posicion((11,5))
        self.parent.jugador.cambiar_direccion(Personaje.SUR)
        self.personajes = [self.parent.jugador, self.ordenador]
        self.mundo = Mundo(self.mapa, self.personajes)

    def start(self):
        print "GameState Mapa2 Started"
        
    def cleanUp(self):
        print "GameState Mapa2 Cleaned"
    
    def pause(self):
        print "GameState Mapa2 Paused"
        pass

    def resume(self):
        print "GameState Mapa2 Resumed"
        pass
    
    def handleEvents(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.parent.pushState(menustate.MenuState(self.parent))
                elif event.key == pygame.K_UP:
                    self.mundo.mover_jugador(Personaje.NORTE)
                elif event.key == pygame.K_DOWN:
                    self.mundo.mover_jugador(Personaje.SUR)
                elif event.key == pygame.K_RIGHT:
                    self.mundo.mover_jugador(Personaje.ESTE)
                elif event.key == pygame.K_LEFT:
                    self.mundo.mover_jugador(Personaje.OESTE)
                    
        k = pygame.key.get_pressed()
        if k[K_UP]: self.mundo.mover_jugador(Personaje.NORTE)
        elif k[K_DOWN]: self.mundo.mover_jugador(Personaje.SUR)
        elif k[K_RIGHT]: self.mundo.mover_jugador(Personaje.ESTE)
        elif k[K_LEFT]: self.mundo.mover_jugador(Personaje.OESTE)


    def update(self):
        self.mundo.update()
        #si el jugador sale por la puerta cargamos el otro mapa
        if(self.parent.jugador.obtener_posicion() == (10,5)):
            self.parent.pushState(mapa1state.Mapa1State(self.parent))
            
    def draw(self):
        self.parent.screen.blit(self.parent.background,(0,0))
        self.mundo.dibujar(self.parent.screen)
