#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class fondo:
	def __init__(self):
		escalado = (800,600)
		escalado_vida = (200,50)
		self.back = [pygame.transform.scale(pygame.image.load("img/fondo_0.png").convert_alpha(),escalado)]
		self.front = [pygame.transform.scale(pygame.image.load("img/fondo_1.png").convert_alpha(),escalado),
					pygame.transform.scale(pygame.image.load("img/fondo_2.png").convert_alpha(),escalado),
					pygame.transform.scale(pygame.image.load("img/fondo_3.png").convert_alpha(),escalado)]
		self.vida = [pygame.transform.scale(pygame.image.load("img/load_back.png").convert_alpha(),escalado_vida),
					pygame.transform.scale(pygame.image.load("img/load.png").convert_alpha(),escalado_vida)]

	def draw_back(self,surf):
		for k in self.back:
	   		surf.blit(k, (0, 0))

 	def draw_front(self,surf):
 		for k in self.front:
 			surf.blit(k,(0,0))
 		for k in self.vida:
 			surf.blit(k,(10,10))

 	def actualizarVida(self,porcentaje):
 		if porcentaje>0:
 			self.vida[1] = pygame.transform.scale(self.vida[1],[2*porcentaje,50])
 		else:
 			self.vida[1] = pygame.transform.scale(self.vida[1],[0,50])