#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random

class rectangulo:
	def __init__(self):
		self.pos = [400,170]
		self.color = [255,255,255]
		self.tam = [100,250]
		self.superficie = pygame.Surface(self.tam)
		self.superficie.fill(self.color)
		imagen = pygame.image.load("img/hombre_0.png").convert_alpha()
		self.img = pygame.transform.scale(imagen,self.tam)
		self.superficie.blit(self.img,(0,0))
		self.t = 0
		self.estado = [0,0]

	def draw(self,surf):
		surf.blit(self.superficie,self.pos)

	def pintarSobre(self,surf,pos):
		self.superficie(surf,pos)

	def move(self,vector):
		self.pos[0] = self.pos[0] + vector[0]
		self.pos[1] = self.pos[1] + vector[1]

	def getPos(self):
		return self.pos

	def choque(self,pos,tam):
		if (pos[0]+tam[0]<self.pos[0] or pos[0]>self.pos[0]+self.tam[0] or pos[1]>self.pos[1]+self.tam[1] or pos[1]+tam[1]<self.pos[1]):
			return False
		else:
			return True

	def toCentro(self):
		#print "A centro"
		if (400-self.tam[0]/2+20<=self.pos[0] and 400-self.tam[0]/2+20>=self.pos[0]):
			self.estado = [0,0]
		else:
			#print self.estado
			self.move([self.estado[1],0])

	def toIzq(self):
		#print "A izquierda"
		if (200-self.tam[0]/2+20<=self.pos[0] and 200-self.tam[0]/2+20>=self.pos[0]):
			self.estado = [0,0]
		else:
			#print self.estado
			self.move([self.estado[1],0])

	def toDer(self):
		#print "A derecha"
		if (600-self.tam[0]/2+20<=self.pos[0] and 600-self.tam[0]/2+20>=self.pos[0]):
			self.estado = [0,0]
		else:
			#print self.estado
			self.move([self.estado[1],0])

	def actualizar(self):
		self.t += 1
		estado = self.estado[0]
		if (estado == 1):
			self.toCentro()
		elif (estado == 2):
			self.toIzq()
		elif (estado == 3):
			self.toDer()
		if self.t > 20:
			self.randomState()
			self.t = 0

	def setEstado(self,estado):
		velocidad = 5
		desplz = 0
		estado_array = [0,0]
		if estado == 0:
			estado_array = [0,0]
		elif estado == 1:
			if (self.pos[0]>400):
				estado_array = [1,-velocidad]
			else:
				estado_array = [1,velocidad]
		elif estado == 2:
			if (self.pos[0]>50):
				estado_array = [2,-velocidad]
			else:
				estado_array = [2,velocidad]
		elif estado == 3:
			if (self.pos[0]>750):
				estado_array = [3,-velocidad]
			else:
				estado_array = [3,velocidad]

		self.estado = estado_array

	def randomState(self):
		estado = int(random.randrange(100))
		if (estado <4):
			self.setEstado(estado)