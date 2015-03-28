#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from pelota import Tpelota

screen = pygame.display.set_mode((640,480))
timer = pygame.time.Clock()
pelotas = [Tpelota([60,120],0),Tpelota([120,180],1),Tpelota([180,240],0),
Tpelota([240,300],1),Tpelota([300,360],0),Tpelota([360,420],1)]

while True:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	screen.fill([0,0,0])
	for k in pelotas:
		k.pintar(screen)
	timer.tick(28)
	pygame.display.update()

