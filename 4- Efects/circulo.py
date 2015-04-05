import pygame

class circulo():
	def __init__(self,radio,grosor,pos,color):
		self.r = radio
		self.b = grosor
		self.pos = pos
		self.color = color
	def draw(self,surface):
		pygame.draw.circle(surface, self.color , self.pos, self.r, self.b)
	def setPos(self,pos):
		self.pos = pos
	def toString(self):
		return self.r,self.b,self.pos,self.color
	def ampliar(self,dr):
		self.r += dr
		if self.r>1200:
			self.r = 2
