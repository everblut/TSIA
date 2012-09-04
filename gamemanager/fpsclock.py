#! /usr/bin/env python2

import pygame.time

class FpsClock:
    "clase para manejar los FPS"
    def __init__(self,fps_deseados=30,haz_reporte=0):
        "crea un FpsClock, proporciona los fps deseados y su reporte"
        self.haz_reporte = haz_reporte
        self.frame_count = 0
        self.frame_timer = pygame.time.get_ticks()
        self.frame_delay = 0
        self.last_tick = pygame.time.get_ticks()
        self.set_fps(fps_deseados)
        self.current_fps = 0.0

    def set_fps(self, fps_deseados):
        "frames per second deseados"
        if fps_deseados:
           #intento de hacerlo mas smooth
            self.fps_ticks = int((0.975/fps_deseados) * 1000)
        else:
            self.fps_ticks = 0
        self.fps_deseados = fps_deseados

    def tick(self):
        "se llama un tick por cada frame"
        #detiene hasta que los mseconds del frame pasen
        if self.fps_ticks:
            now = pygame.time.get_ticks()
            wait = self.fps_ticks - ( now - self.last_tick )
            pygame.time.delay(wait)
            self.frame_delay += wait
        self.last_tick = pygame.time.get_ticks()

        #refresca current_fps
        self.frame_count += 1
        time = self.last_tick - self.frame_timer
        if time > 1000:
            time -= self.frame_delay
            if not time: self.current_fps = 1.0
            else: self.current_fps = self.frame_count / (time/1000.0)
            
            self.frame_count = 0
            self.frame_delay = 0
            self.frame_timer = self.last_tick
            if self.haz_reporte: self.reporte()

    def reporte(self):
        "sobrecarga para visualizar un mejor reporte de FPS "
        estimado = (0,0)
        if (self.current_fps > 0):
            estimado = 1.0/self.current_fps, self.current_fps
        return 'Tiempo Promedio: %.3f    FPS: %.2f' % estimado
