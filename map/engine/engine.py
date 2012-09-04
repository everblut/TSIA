#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *

from maps import *

# Constantes
WIDTH = 640
HEIGHT = 480

# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def salir():
	keys = pygame.key.get_pressed()
	for eventos in pygame.event.get():
		if eventos.type == QUIT:
			sys.exit(0)
		if keys[K_ESCAPE]:
			sys.exit(0)

# ---------------------------------------------------------------------

def main():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Engine RPG")

	clock = pygame.time.Clock()
	
	mapa = Mapa("bosque.tmx")
	print mapa.tileset

	while True:
		time = clock.tick(60)
		salir()

		pygame.display.flip()
	return 0

if __name__ == '__main__':
	pygame.init()
	main()
