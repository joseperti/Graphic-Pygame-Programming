import pygame
import math
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

class circulo:

	def __init__(self,radio,centro,evol):
		self.evol = evol
		self.centro = centro
		self.radio = radio
		self.color = [0,0,200]

	def partir(self):
		nuevos = []

		nuevo_radio = (int) (self.radio * 5/10)
		if nuevo_radio<1:
			nuevo_radio = 0
		nuevo_centro = [self.centro[0]-nuevo_radio-self.radio,self.centro[1]]
		circulo_L = circulo(nuevo_radio,nuevo_centro,"L")

		nuevo_centro = [self.centro[0],self.centro[1]+nuevo_radio+self.radio]
		circulo_U = circulo(nuevo_radio,nuevo_centro,"U")

		nuevo_centro = [self.centro[0],self.centro[1]-nuevo_radio-self.radio]
		circulo_D = circulo(nuevo_radio,nuevo_centro,"D")

		nuevo_centro = [self.centro[0]+nuevo_radio+self.radio,self.centro[1]]
		circulo_R = circulo(nuevo_radio,nuevo_centro,"R")

		if self.evol == "L":
			nuevos = [circulo_L,circulo_U,circulo_D]
		elif self.evol == "R":
			nuevos = [circulo_R,circulo_U,circulo_D]
		elif self.evol == "U":
			nuevos = [circulo_L,circulo_U,circulo_R]
		elif self.evol == "D":
			nuevos = [circulo_R,circulo_L,circulo_D]
		elif self.evol == "T":
			nuevos = [circulo_R,circulo_L,circulo_D,circulo_U]

		if (nuevo_radio>0):
			return nuevos

	def draw(self,surf):
		pygame.draw.circle(surf, self.color, self.centro,self.radio,0)

	def drawAura(self,surf):
		for k in range(self.radio/2,1,-(int) (self.radio/5)):
			print "Pintar aura"
			pr = (int)(255/ k)
			print pr
			color = [pr,pr,pr]
			pygame.draw.circle(surf, color, self.centro,self.radio+k,0)