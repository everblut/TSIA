#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
from pygame.locals import *
from xml.dom import minidom, Node

from funciones import *
from engine import WIDTH, HEIGHT


# Clases
# ---------------------------------------------------------------------

class Mapa:
	def __init__(self, nombre):
		self.nombre = nombre
		self.capas = []
		
		self.cargar_mapa() # Inicializa los valores desde el xml.
		
		self.tileset = cortar_tileset("graphics/tilesets/"+self.tileset, self.tam_tiles)
		

	# Extrae valores mapa desde XML.	
	def cargar_mapa(self):
		xmlMap = minidom.parse("maps/"+self.nombre)
		nPrincipal = xmlMap.childNodes[0]
		
		# Tamaño mapa
		self.width = int(nPrincipal.attributes.get("width").value)
		self.height = int(nPrincipal.attributes.get("height").value)
		
		for i in range(len(nPrincipal.childNodes)):
			if nPrincipal.childNodes[i].nodeType == 1:
				if nPrincipal.childNodes[i].nodeName == "tileset":
					if nPrincipal.childNodes[i].attributes.get("name").value != "config":
						width = nPrincipal.childNodes[i].attributes.get("tilewidth").value
						height = nPrincipal.childNodes[i].attributes.get("tileheight").value
						nombre = nPrincipal.childNodes[i].childNodes[1].attributes.get("source").value
						nombre = extraer_nombre(nombre)
						self.tileset = nombre
					self.tam_tiles = (int(width), int(height))
				if nPrincipal.childNodes[i].nodeName == "layer":
					if  nPrincipal.childNodes[i].attributes.get("name").value != "colisiones":
						layer = nPrincipal.childNodes[i].childNodes[1].childNodes[0].data.replace("\n", "").replace(" ", "")
						layer = decodificar(layer) # Decodifica la lista
						layer = convertir(layer, self.width) # Convierta en array bidimensional
						self.capas.append(layer)
				if nPrincipal.childNodes[i].nodeName == "objectgroup":
					x = nPrincipal.childNodes[i].childNodes[1].attributes.get("x").value
					y = nPrincipal.childNodes[i].childNodes[1].attributes.get("y").value
					self.start = (int(x), int(y))

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# Convierta una array unidimensional en una bidimensional.
def convertir(lista, col):
	nueva = []
	for i in range(0, len(lista), col):
		nueva.append(lista[i:i+col])
	return nueva

# Extra el nombre de un archivo de una ruta.	
def extraer_nombre(ruta):
	a = -1
	for i in range(len(ruta)):
		if ruta[i] == "/" or ruta[i] == "\\":
			a = i
	if a == -1:
		return ruta
	return ruta[a+1:]

# ---------------------------------------------------------------------

def main():
	return 0

if __name__ == '__main__':
	main()
