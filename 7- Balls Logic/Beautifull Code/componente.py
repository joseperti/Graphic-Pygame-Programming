#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import math

class TComponente:
	def __init__(self,posicion,radio,color):
		self.posicion = posicion
		self.radio = radio
		self.color = color

	def pintar(self,screen):
		pygame.draw.circle(screen,self.color,self.posicion,self.radio)

	def mouseOver(self,posMouse):
		if self.distancia(posMouse,self.posicion)<= self.radio:
			return True
		else:
			return False

	def distancia(self,punto1,punto2):
		return (math.sqrt((punto1[0]-punto2[0])**2 + (punto1[1]-punto2[1])**2))

	def setPos(self,posicion):
		self.posicion = posicion

	def getPos(self):
		return self.posicion

	def getRadio(self):
		return self.radio