#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class fondo:
	def __init__(self):
		escalado = (800,600)
		self.back = [pygame.transform.scale(pygame.image.load("img/fondo_0.png").convert_alpha(),escalado)]
		self.front = [pygame.transform.scale(pygame.image.load("img/fondo_1.png").convert_alpha(),escalado),
					pygame.transform.scale(pygame.image.load("img/fondo_2.png").convert_alpha(),escalado),
					pygame.transform.scale(pygame.image.load("img/fondo_3.png").convert_alpha(),escalado)]

	def draw_back(self,surf):
		for k in self.back:
	   		surf.blit(k, (0, 0))

 	def draw_front(self,surf):
 		for k in self.front:
 			surf.blit(k,(0,0))