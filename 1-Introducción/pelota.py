#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import math
from pygame.locals import *
class Tpelota:
	def __init__(self,inicial,giro):
		self.radio = 10
		self.color = [255,40,40]
		self.pos = [320,240]
		self.pos_ini = inicial
		self.tiempo = 0
		self.giro = giro
	def pintar(self,surf):
		self.actualizar()
		pygame.draw.circle(surf,self.color,self.pos,self.radio)
		self.control_tiempo()
	def actualizar(self):
		if self.giro == 0:
			self.pos[0] = self.pos_ini[0]+int(50*math.sin(self.tiempo*(2*3.1415/28)))
			self.pos[1] = self.pos_ini[1] + int(50*math.cos(self.tiempo*(2*3.1415/28)))
		else:
			self.pos[1] = self.pos_ini[1]+int(50*math.sin(self.tiempo*(2*3.1415/28)))
			self.pos[0] = self.pos_ini[0] + int(50*math.cos(self.tiempo*(2*3.1415/28)))
	def control_tiempo(self):
		self.tiempo += 1
		if self.tiempo>28:
			self.tiempo = 0