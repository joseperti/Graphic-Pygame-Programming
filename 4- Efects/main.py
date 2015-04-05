#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from ondas import *
from circulo import *
from pygame.locals import *

def eventos():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0]:
				listado.put(circulo(2,2,pygame.mouse.get_pos(),[0,0,255]))

pygame.init()
screen = pygame.display.set_mode((1366,768))
timer = pygame.time.Clock()
listado = ondas()
#c1 = circulo(200,2,[320,240])
#listado.put(c1)
listado.test()
while True:
	eventos()

	listado.pintar(screen)
	listado.avance()
	pygame.display.flip()
	timer.tick(100)
