#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class hand:
	def __init__(self):
		self.img = pygame.image.load("img/hand_0.png").convert_alpha()
		self.pos = [400,200]

	def draw(self,surf):
	   	surf.blit(self.img, self.pos)

	def setPos(self,pos):
		self.pos = pos

	def getPos(self):
		return [self.pos[0]+200,self.pos[1]]