from circulo import *
from pygame import *

class ondas:
	def __init__(self):
		self.array = []

	def pintar(self,surface):
		surface.fill([0,71,171])
		for k in self.array:
			k.draw(surface)

	def put(self,element):
		self.array.append(element)

	def avance(self):
		for k in self.array:
			k.ampliar(1)
	
	def test(self):
		self.array = [circulo(50,2,[683,384],[0,0,255]),circulo(100,2,[683,384],[0,0,255]),
		circulo(150,2,[683,384],[0,0,255]),circulo(200,2,[683,384],[0,0,255]),
		circulo(250,2,[683,384],[0,0,255]),circulo(300,2,[683,384],[0,0,255])]