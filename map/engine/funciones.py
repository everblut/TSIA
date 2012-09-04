#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import base64
import gzip
import StringIO
import pygame
from pygame.locals import *


# Mapas
# ---------------------------------------------------------------------

def decodificar(cadena):
	# Decodificar.
	cadena = base64.decodestring(cadena)
	
	# Descomprimir.
	copmressed_stream = StringIO.StringIO(cadena)
	gzipper = gzip.GzipFile(fileobj=copmressed_stream)
	cadena = gzipper.read()
	
	# Convertir.
	salida = []
	for idx in xrange(0, len(cadena), 4):
		val = ord(str(cadena[idx])) | (ord(str(cadena[idx + 1])) << 8) | \
		(ord(str(cadena[idx + 2])) << 16) | (ord(str(cadena[idx + 3])) << 24)
		salida.append(val)
		
	return salida

# ---------------------------------------------------------------------

# Pygame
# ---------------------------------------------------------------------

# Carga una imagen transparencia y color tranasparente opcionales.
def load_image(filename, transparent=False, pixel=(0,0)):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at(pixel)
                image.set_colorkey(color, RLEACCEL)
        return image

# Corta un tilest y lo almacena en un array unidimensional.  
def cortar_tileset(ruta, (w, h)):
	image = load_image(ruta, True)
	rect = image.get_rect()
	col = rect.w / w
	fil = rect.h / h
	sprite = [None]
		
	for f in range(fil):
		for c in range(col):
			sprite.append(image.subsurface((rect.left, rect.top, w, h)))
			rect.left += w
		rect.top += h
		rect.left = 0
		
	return sprite

# ---------------------------------------------------------------------
