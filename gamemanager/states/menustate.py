#! /usr/bin/env python2

import pygame
from pygame.locals import *
from gamemanager.states import gamestate,pantallastate,opcionesstate

class MenuState(gamestate.GameState):
    
    def __init__(self,parent):
        self.parent = parent
        self.background = pygame.Surface(self.parent.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((255,0,0))
        
    def start(self):
        print "GameState Menu started"
    
    def cleanUp(self):
        print "GameState Menu Cleaned"
        pass

    def pause(self):
        print "GameState Menu Paused"
        pass

    def resume(self):
        print "GameState Menu Resumed"
        pass

    def handleEvents(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.parent.quit()
                elif event.key == pygame.K_p:
                    self.parent.pushState(pantallastate.PantallaState(self.parent))
                elif event.key == pygame.K_o:
                    self.parent.pushState(opcionesstate.OpcionesState(self.parent))
    def update(self):
        pass
    
    def draw(self):
        self.parent.screen.blit(self.background, (0,0))



        
