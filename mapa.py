#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Modulos
from xml.dom import minidom
import base64
import gzip
import StringIO
from utilidades.imagen import *
from utilidades.archivo import *


#clase

class Mapa:
    
    LAYER_PISABLE = 0
    LAYER_SUELO = 1
    LAYER_OBJETOS = 2
    LAYER_OBJETOS_SUPERPUESTOS = 3
    LAYER_CIELO = 4

    def __init__(self, nombre):
        self.nombre = nombre
        self.capas = []

        self.cargar_mapa()
        self.tileset = cortar_tileset("data/imagenes/"+self.tileset, self.tam_tiles, True)

    def cargar_mapa(self):
        xmlMap = minidom.parse("data/mapas/"+self.nombre)
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
                        if nPrincipal.childNodes[i].attributes.get("name").value == "tileset":
                            self.tileset = nombre                            
                    self.tam_tiles = (int(width), int(height))
                if nPrincipal.childNodes[i].nodeName == "layer":
                    layer = nPrincipal.childNodes[i].childNodes[1].childNodes[0].data.replace("\n", "").replace(" ", "")
                    layer = self.decodificar(layer) # Decodifica la lista
                    layer = self.convertir(layer, self.width) # Convierta en array bidimensional                        
                    self.capas.append(layer)

   

# convierte un array unidimensional en un bidimensional
    def convertir(self,lista, col):
        nueva = []
        for i in range(0, len(lista), col):
            nueva.append(lista[i:i+col])
        return nueva

#decodifica y descomprime un mapa

    def decodificar(self,cadena):
    #decodifica
        cadena = base64.decodestring(cadena)
    #descomprime
        cadena_comprimida = StringIO.StringIO(cadena)
        gzipper = gzip.GzipFile(fileobj=cadena_comprimida)
        cadena = gzipper.read()
    #convertir
        salida = []
        for idx in xrange(0, len(cadena), 4):
            val = ord(str(cadena[idx])) | (ord(str(cadena[idx+1])) << 8) | \
                (ord(str(cadena[idx+2])) << 16) | (ord(str(cadena[idx+3])) << 24)
            salida.append(val)
        return salida

    def dibujar(self, capa, dest, x, y):
        '''Dibuja una capa del pama en una surface'''
        x_aux = x
        y_aux = y

        for f in range(self.height):
            for c in range(self.width):
                if self.capas[capa][f][c]:
                    dest.blit(self.tileset[self.capas[capa][f][c]],(x_aux,y_aux))
                x_aux = x_aux + self.tam_tiles[0]
            y_aux = y_aux + self.tam_tiles[1]
            x_aux = x

    def obtener_centro_celda(self,fila,columna):
        x = (self.tam_tiles[0] * columna ) + (self.tam_tiles[0] /2 )
        y = (self.tam_tiles[1] * fila ) + (self.tam_tiles[1] / 2)
        return (x,y)
    
    def es_pisable(self,fila,columna):
        #si se intenta mover fuera del mapa, no se permite
        if ((fila >= self.height) or (fila < 0) or (columna >= self.width) or (columna < 0 )):
            return False
        else:
            return not (self.capas[Mapa.LAYER_PISABLE][fila][columna])
