#! /usr/bin/env python2

import pygame
from pygame.locals import *
from gamemanager.states import gamestate

class OpcionesState(gamestate.GameState):

    def __init__(self,parent):
        self.parent = parent
        self.background = pygame.Surface(self.parent.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,255,0))
        
    def start(self):
        print "GameState Opciones Started"
    
    def cleanUp(self):
        print "GameState Opciones Cleaned"
        pass

    def pause(self):
        print "GameState Opciones Paused"
        pass

    def resume(self):
        print "GameState Opciones Resumed"
        pass

    def handleEvents(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.parent.popState()

    def update(self):
        pass

    def draw(self):
        self.parent.screen.blit(self.background, (0,0))
