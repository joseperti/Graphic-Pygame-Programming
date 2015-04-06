
import pygame
from pygame.locals import *
from triangulo import *


screen = pygame.display.set_mode((800,600))
timer = pygame.time.Clock()
triangulos = []
triangulos.append(triangulo([10,10],[100,500],[700,50]))

def actualizar(triangulos):
	nuevo = []
	for k in triangulos:
		datos = k.partir()
		nuevo.append(datos[0])
		nuevo.append(datos[1])

	return nuevo

def pintar(triangulos):
	for k in triangulos:
		k.draw(screen)
m = 0
max = 10
act = True
while (m<max):
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == pygame.KEYDOWN:
			if act:
				act = False
			else:
				act = True

	if act:
		m += 1
		screen.fill([255,255,255])
		pintar(triangulos)
		triangulos = actualizar(triangulos)
	pygame.display.update()
	timer.tick(1)
