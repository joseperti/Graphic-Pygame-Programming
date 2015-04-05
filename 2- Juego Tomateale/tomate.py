#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class tomatoe:
	def __init__(self):
		self.imgIni = pygame.image.load("img/tomate.png").convert_alpha()
		self.posIni = [0,0]
		self.posFin = [0,0]
		self.pos = [0,0]
		self.tamIni = [100,100]
		self.tamFin = [20,20]
		self.tam = [0,0]
		self.v = [0,0,0,0]
		self.tiempo = 10
		self.estado = 0
		self.img = pygame.transform.scale(self.imgIni,self.tamIni)
		self.img_mancha = pygame.transform.scale(pygame.image.load("img/mancha.png").convert_alpha(),self.tamFin)
		self.timer = 0

	def getPos(self):
		return self.pos

	def getTam(self):
		return self.tam

	def draw(self,surf):
	   	surf.blit(self.img, [int(self.pos[0]),int(self.pos[1])])

	def setPosIni(self,pos):
		self.posIni = pos

	def setPosFin(self,pos):
		self.posFin = pos

	def setTamIni(self,tam):
		self.tamIni = tam
		self.img = pygame.transform.scale(self.imgIni,self.tamIni)

	def setTamFin(self,tam):
		self.tamFin = tam

	def crearTomate(self):
		self.timer = 0
		self.tomate = 0
		self.img = pygame.transform.scale(self.imgIni,self.tamIni)
		self.v = [(self.posIni[0]-self.posFin[0])/self.tiempo,(self.posIni[1]-self.posFin[1])/self.tiempo,
				(self.tamIni[0]-self.tamFin[0])/self.tiempo,(self.tamIni[1]-self.tamFin[1])/self.tiempo]
		self.tam = self.tamIni
		self.pos = self.posIni

	def actualizar(self):
		if not(self.tam[0] <= self.tamFin[0]+20 and self.tam[0] >= self.tamFin[0]-20):
			self.pos = [self.pos[0]-self.v[0],self.pos[1]+self.v[1]]
			self.tam = [self.tam[0]-self.v[2],self.tam[1]-self.v[3]]
			self.img = pygame.transform.scale(self.imgIni,[int(self.tam[0]),int(self.tam[1])])
			return False
		else:
			self.timer += 1
			self.img = self.img_mancha
			if (self.timer>20):
				return True
			else:
				return False