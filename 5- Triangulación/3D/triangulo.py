import pygame
import math
import random

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2 +  (p0[2] - p1[2])**2)

def vectorNormal(p0,p1,p2):
	v1 = [p1[0]-p0[0],p1[1]-p0[1],p1[2]-p0[2]]
	v2 = [p2[0]-p0[0],p2[1]-p0[1],p2[2]-p0[2]]
	vector = [(v1[1]*v2[2] - v1[2]*v2[1])	,
				v2[0]*v1[2] - v1[0]*v2[2],
				v1[0]*v2[1] - v2[0]*v1[1]]
	return vector

def anguloOY(vector):
	if vector[1]==0:
		return 0
	else:
		return abs(math.acos((vector[1])/math.sqrt((vector[0])**2+(vector[1])**2+(vector[2])**2)))

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
		self.vNormal = vectorNormal(self.A,self.B,self.C)
		self.angulo = anguloOY(self.vNormal)
		self.color = [0,255 * self.angulo/3.15,0]
		
		coef = 0.1
		self.pr_A = [self.A[0],self.A[1]*coef + self.A[2]]
		self.pr_B = [self.B[0],self.B[1]*coef + self.B[2]]
		self.pr_C = [self.C[0],self.C[1]*coef+ self.C[2]]

	def partir(self):
		nuevo_punto = [(int) (self.A[0] + self.B[0])/2,
						(int) (self.A[1] + self.B[1])/2,
						(int) ((self.A[2] + self.B[2])/2) + random.randrange(-10,10,1)]
		#print "Nuevo punto"
		#print nuevo_punto
		return [triangulo(self.A,nuevo_punto,self.C),
				triangulo(nuevo_punto,self.C,self.B),
				triangulo(self.A,self.B,nuevo_punto)]

	def draw(self,surf):		

		#Primer cuadrante superior

		pygame.draw.polygon(surf, self.color, [[self.A[0],300-self.A[1]],[self.B[0],300-self.B[1]],[self.C[0],300-self.C[1]]],0)

		'''
		pygame.draw.line(surf, self.color, [self.A[0],300-self.A[1]], [self.B[0],300-self.B[1]])
		pygame.draw.line(surf, self.color, [self.B[0],300-self.B[1]], [self.C[0],300-self.C[1]])
		pygame.draw.line(surf, self.color, [self.A[0],300-self.A[1]], [self.C[0],300-self.C[1]])
		'''
		
		#Segundo cuadrante vista Z +400

		pygame.draw.polygon(surf, self.color, [[self.A[0]+400,300-self.A[2]],[self.B[0]+400,300-self.B[2]],[self.C[0]+400,300-self.C[2]]],0)

		'''
		pygame.draw.line(surf, self.color, [self.A[0]+400,300-self.A[2]], [self.B[0]+400,300-self.B[2]])
		pygame.draw.line(surf, self.color, [self.B[0]+400,300-self.B[2]], [self.C[0]+400,300-self.C[2]])
		pygame.draw.line(surf, self.color, [self.A[0]+400,300-self.A[2]], [self.C[0]+400,300-self.C[2]])
		'''

		#Primer cuadrante abajo vista inclinada

		pygame.draw.polygon(surf, self.color, [[self.pr_A[0],600-self.pr_A[1]],[self.pr_B[0],600-self.pr_B[1]],[self.pr_C[0],600-self.pr_C[1]]],0)
