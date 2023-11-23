#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

import copy
import random
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

def seguidos(lista):
	#print lista
	orden = True
	for k in range(1,len(lista)-1,1):
		if lista[k] == len(lista)-1:
			if lista[k+1] == 0:
				#print "okey"
				None
			else:
				orden = False
		elif lista[k] == 0:
			if lista[k+1] == lista[k]+1:
				#print "okey"
				None
			else:
				orden = False
		else:
			if lista[k+1] == lista[k]+1 and lista[k-1] == lista[k]-1:
				#print "okey"
				None
			else:
				orden = False
	if orden:
		return orden
	else:
		#Comprobamos si son descendientes
		orden = True
		for k in range(1,len(lista)-1,1):
			if lista[k] == len(lista)-1:
				if lista[k-1] == 0:
					#print "okey"
					None
				else:
					orden = False
			elif lista[k] == 0:
				if lista[k-1] == lista[k]+1:
					#print "okey"
					None
				else:
					orden = False
			else:
				if lista[k-1] == lista[k]+1 and lista[k+1] == lista[k]-1:
					#print "okey"
					None
				else:
					orden = False
		return orden



pygame.init()
screen = pygame.display.set_mode((640,480))
maximo = 4
nivel = 1
salir = False

def inicio():
	aleatorio = random.randrange(1,maximo,1)
	componentes = []
	for l in range(aleatorio):
		componentes.append(TComponente([random.randrange(40,600,10),random.randrange(40,440,10)],random.randrange(5,30,5)
		,[random.randrange(0,250,10),random.randrange(0,250,10),random.randrange(0,250,10)]))
	lineas = []

	for k in range(len(componentes)-1):
		lineas.append([componentes[k],componentes[k+1]])
	lineas.append([componentes[0],componentes[len(componentes)-1]])

	huecos = []
	for l in range(aleatorio):
		huecos.append(THueco([random.randrange(40,600,10),random.randrange(40,440,10)],componentes[l].getRadio()+10,[50,50,50]))
	lineas_huecos = []
	for k in range(len(huecos)-1):
		lineas_huecos.append([huecos[k],huecos[k+1]])
	lineas_huecos.append([huecos[0],huecos[len(huecos)-1]])
	huecosSurf = pygame.Surface((640,480), pygame.SRCALPHA, 32)

	for lh in lineas_huecos:
			pygame.draw.line(huecosSurf,[50,50,50],lh[0].getPos(),lh[1].getPos(),10)
	for h in huecos:
		h.pintar(huecosSurf)
	huecosScaled = pygame.transform.scale(huecosSurf,(128,96))

	mover = -1
	juego = True
	
	'''font = pygame.font.Font(None, 20)
	textNivel = font.render("Level: %s" %(nivel), 1, (10, 100, 10))
	textSpaceBar = font.render("Press Space Bar to confirm", 1, (10, 100, 10))'''

	while juego:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				juego = False
				global salir
				salir = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					copia = copy.copy(componentes)
					ordenacion = []
					for k in huecos:
						obtenido = k.getCol(copia)
						if obtenido != None:
							#print "Uno acertado"
							ordenacion.append(componentes.index(obtenido))
							copia.remove(obtenido)
						else:
							#print "U Lose!"
							break
					if len(copia) == 0:
						#print "Has ganado!!!"
						#print "Comprobando el orden:"
						if seguidos(ordenacion):
							juego = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				posicion = pygame.mouse.get_pos()
				n = 0
				for k in componentes:
					if k.mouseOver(posicion):
						mover = n
						break
					else:
						n+=1
			elif event.type == pygame.MOUSEBUTTONUP:
				mover = -1

		if mover!=-1:
			componentes[mover].setPos(pygame.mouse.get_pos())
		screen.fill([255,255,255])
		screen.blit(huecosSurf,[0,0])
		for l in lineas:
			pygame.draw.line(screen,[50,50,250],l[0].getPos(),l[1].getPos(),5)
		for k in componentes:
			k.pintar(screen)
		'''screen.blit(textNivel,(0,0))
		screen.blit(textSpaceBar,(20,460))'''
		pygame.display.update()

while not(salir):
	inicio()
	maximo += 1
	nivel += 1