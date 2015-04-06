
import pygame
from pygame.locals import *
from triangulo import *


screen = pygame.display.set_mode((800,600))
timer = pygame.time.Clock()
triangulos = []
'''
triangulos.append(triangulo([10,10,100],[100,250,100],[300,50,100]))
triangulos.append(triangulo([400,200,200],[100,250,100],[300,50,100]))
'''
triangulos.append(triangulo([0,0,0],[400,0,0],[0,300,0]))
triangulos.append(triangulo([400,300,0],[400,0,0],[0,300,0]))

def actualizar(triangulos):
	nuevo = []
	for k in triangulos:
		datos = k.partir()
		nuevo.append(datos[0])
		nuevo.append(datos[1])

	return nuevo

def pintar(triangulos):
	color = [0,0,255]
	pygame.draw.line(screen,color, [400,0],[400,600])
	pygame.draw.line(screen,color, [0,300],[800,300])
	for k in triangulos:
		k.draw(screen)

m = 0
max = 10
act = True
while (m<max):
	#print "Cantidad de triangulos: ",len(triangulos)
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
	else:
		pygame.display.update()
		timer.tick(28)
