#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import math

class THueco:
	def __init__(self,posicion,radio,color):
		self.posicion = posicion
		self.radio = radio
		self.color = color

	def pintar(self,screen):
		pygame.draw.circle(screen,self.color,self.posicion,self.radio)

	def distancia(self,punto1,punto2):
		return (math.sqrt((punto1[0]-punto2[0])**2 + (punto1[1]-punto2[1])**2))

	def setPos(self,posicion):
		self.posicion = posicion

	def getPos(self):
		return self.posicion

	def getCol(self,componentes):
		interior = None
		dMin = self.radio + 1
		for k in componentes:
			distancia = self.distancia(self.getPos(),k.getPos())
			difRadio = abs(self.radio - k.getRadio())
			if distancia < difRadio:
				if distancia < dMin:
					interior = k
					dMin = distancia
		if interior!=None:
			#print "Hay colision"
			None
		return interior