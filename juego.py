#!/usr/bin/env python2

import pygame
from pygame.locals import *

from gamemanager.gamemanager import GameManager
from gamemanager.states import menustate
from gamemanager.fpsclock import *

if __name__ == "__main__":
    
    game = GameManager('Juego python',(640,480),False)
    game.changeState(menustate.MenuState(game))
    fps = FpsClock(35,0)
    
    while game.running:
        game.handleEvents(pygame.event.get())
        game.update()
        game.draw()
        fps.tick()
        
    game.cleanUp()
