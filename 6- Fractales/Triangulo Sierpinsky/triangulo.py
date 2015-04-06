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

		print self.A
		print self.B
		print self.C

		medio_AB = [(int) (self.A[0] + self.B[0])/2,
						(int) (self.A[1] + self.B[1])/2]
		medio_AC = [(int) (self.A[0] + self.C[0])/2,
						(int) (self.A[1] + self.C[1])/2]
		medio_CB = [(int) (self.C[0] + self.B[0])/2,
						(int) (self.C[1] + self.B[1])/2]

		print medio_AB
		print medio_AC
		print medio_CB
		return [triangulo(self.A,medio_AB,medio_AC),
				triangulo(self.B,medio_AB,medio_CB),
				triangulo(self.C,medio_CB,medio_AC)]

	def draw(self,surf):
		pygame.draw.polygon(surf, self.color_2, [self.A,self.B,self.C],1)