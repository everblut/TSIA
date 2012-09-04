#! /usr/bin/env python2

import os
import sys
import pygame
from pygame.locals import *
from singleton import *


class GameManager(object):
    
    __metaclass__ = Singleton

    def __init__(self,titulo, size=(320,200), fullscreen=False):
        print "Iniciando el gamemanager"
        
        self.states = []
        self.running = True
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        
        pygame.display.set_caption(titulo)
        pygame.mouse.set_visible(0)
        
    def cleanUp(self):
        while len(self.states) > 0:
            state = self.states.pop()
            state.cleanUp()
        sys.exit(0)

    def changeState(self,gameState):
        print "cambio estado"
        if len(self.states)> 0 :
            state = self.states.pop()
            state.cleanUp()
        self.states.append(gameState)
        self.states[-1].start()
        
    def pushState(self,gameState):
        if len(self.states) > 0:
            self.states[-1].pause()
        self.states.append(gameState)
        self.states[-1].start()

    def popState(self):
        if len(self.states) > 0:
            state = self.states.pop()
            state.cleanUp()
        if len(self.states) > 0:
            self.states[-1].resume()
        
    def handleEvents(self,events):
        self.states[-1].handleEvents(events)
        
    def update(self):
        self.states[-1].update()
        
    def draw(self):
        self.states[-1].draw()
        pygame.display.flip()
        
    def quit(self):
        print "Quit"
        self.running = False
