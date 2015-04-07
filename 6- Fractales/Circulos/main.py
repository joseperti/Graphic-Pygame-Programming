
import pygame
from pygame.locals import *
from circulo import *


screen = pygame.display.set_mode((800,600))
timer = pygame.time.Clock()
circulos = []
circulos.append(circulo(100,[400,600-300],"T"))
sur_circulos = pygame.Surface((800,600)).convert_alpha()
sur_aura = pygame.Surface((800,600)).convert_alpha()

def actualizar(circulos):
	nuevo = []
	for k in circulos:
		datos = k.partir()
		for d_nuevo in datos:
			nuevo.append(d_nuevo)
	return nuevo

def pintar(circulos):
	for k in circulos:
		k.drawAura(sur_aura)
		k.draw(sur_circulos)

	screen.blit(sur_aura,(0,0))
	screen.blit(sur_circulos,(0,0))

m = 0
max = 10
act = True
screen.fill([0,0,0])
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
		pintar(circulos)
		try:
			circulos = actualizar(circulos)
		except:
			m = max
	pygame.display.update()
	timer.tick(1)
print "Fin"

pintar(circulos)

while (act):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if act:
					act = False
				else:
					act = True
	pygame.display.update()
	timer.tick(28)