#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from random import *
from fondo import *
from rectangulo import *
from mano import *
from tomate import *

def clscr():

	print("\n\n\n\n\n\n\n")

print("|     |")
screen = pygame.display.set_mode((800,600))
screen.blit(pygame.image.load("img/present.png"),(0,0))
pygame.display.update()
clscr()
print("|#    |")
timer = pygame.time.Clock()
clscr()
print("|##   |")
background = fondo()
clscr()
print("|###  |")
actor = rectangulo()
clscr()
print("|#### |")
mano = hand()
clscr()
print("|#####|")
tomates = []
t = 0


while (t<100):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	pygame.display.update()
	timer.tick(20)
	t+=1

t = 0

def disparo():
	posicion_mano = mano.getPos()
	tomate = tomatoe()
	tomate.setPosIni([posicion_mano[0]-50,posicion_mano[1]+100])
	tomate.setPosFin([posicion_mano[0] - 260,posicion_mano[1]+120])
	tomate.crearTomate()
	tomates.append(tomate)

while True:
	t += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if t>20:
				disparo()
				t = 0

	tecla = pygame.key.get_pressed()
	screen.fill([255,255,255])
	mano.setPos([pygame.mouse.get_pos()[0],200])
	background.draw_back(screen)
	actor.actualizar()
	actor.draw(screen)
	background.draw_front(screen)
	for tomate in tomates:
		tomate.draw(screen)
		if (actor.choque(tomate.getPos(),tomate.getTam())):
			vida = actor.getVida()
			background.actualizarVida(vida)
		if (tomate.actualizar()):
			tomates.remove(tomate)
	mano.draw(screen)
	timer.tick(28)
	pygame.display.update()



