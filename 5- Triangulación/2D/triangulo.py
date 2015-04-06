import pygame
import math
def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

class triangulo:

	def __init__(self,A,B,C):
		d_AB = distance(A,B)
		d_AC = distance(A,C)
		d_BC = distance(B,C)
		if (d_AB > d_AC and d_AB > d_BC):
			self.A = A
			self.B = B
			self.C = C
		elif (d_AC > d_AB and d_AC > d_BC):
			self.A = A
			self.B = C
			self.C = B
		else:
			self.A = C
			self.B = B
			self.C = A
		self.color = [0,255,0]
		self.color_2 = [0,200,100]

	def partir(self):
		nuevo_punto = [(int) (self.A[0] + self.B[0])/2,
						(int) (self.A[1] + self.B[1])/2]
		print "Nuevo punto"
		print nuevo_punto
		return [triangulo(self.A,nuevo_punto,self.C),
				triangulo(nuevo_punto,self.C,self.B)]

	def draw(self,surf):
		pygame.draw.polygon(surf, self.color_2, [self.A,self.B,self.C],0)

		pygame.draw.line(surf, self.color, self.A, self.B)
		pygame.draw.line(surf, self.color, self.B, self.C)
		pygame.draw.line(surf, self.color, self.C, self.A)