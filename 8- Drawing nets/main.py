import pygame
import math
import random
from pygame.locals import * 

###JOSEPERTI CODE####

class grafo:
    def __init__(self):
        self.num = 200
        self.matriz = []
        self.matriz_pos = []
        self.angulo = (2 * math.pi/self.num)
        self.radio = 300
        self.dim = [840,640]
        self.centro = [self.dim[0]/2,self.dim[1]/2]
        self.surf_base = pygame.Surface(self.dim)
        self.surf = self.surf_base
        self.surf_coord = [0,0]
        for k in range(self.num):
            x = int(self.radio * math.cos(self.angulo * k))+self.centro[0]
            y = int(self.radio * math.sin(self.angulo * k))+self.centro[1]
            self.matriz_pos.append([x,y])
            
    def pintar_nodos(self):
        for k in range(self.num):
            pygame.draw.circle(self.surf,[255,0,0],self.matriz_pos[k],1)
            
    def pintar_arcos(self):
        color = [0,0,100]
        n = 2
        for k in range(self.num):
            for i in range(self.num):
                color[n]+=10
                if color[n]> 250:
                    color[n] = 0
                if (self.matriz[k][i]==1):
                    pygame.draw.line(self.surf,color,self.matriz_pos[k],self.matriz_pos[i])

    def aleatorio(self):
        matriz = []
        for k in range(self.num):
            m_0 = []
            for i in range(self.num):
                num = random.random()
                if num<0.1:
                    m_0.append(1)
                else:
                    m_0.append(0)
            matriz.append(m_0)
        self.matriz = matriz
        #print self.matriz

    def pintar_surf(self,ventana):
        ventana.fill([0,0,0])
        ventana.blit(self.surf, self.surf_coord)

    def mover_surf(self,coord):
        self.surf_coord[0] += coord[0]
        self.surf_coord[1] += coord[1]

    def aumento(self,aum):
        if self.dim[0]+aum[0] >0 and self.dim[1]+aum[1]>0:
            self.dim[0] += aum[0]
            self.dim[1] += aum[1]
            self.surf = pygame.transform.scale(self.surf_base,(self.dim))
        
def main():

    ventana = pygame.display.set_mode((840,640))
    timer = pygame.time.Clock()
    grafo_0 = grafo()
    grafo_0.aleatorio()
    grafo_0.pintar_arcos()
    grafo_0.pintar_nodos()
    grafo_0.pintar_surf(ventana)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
        key = pygame.key.get_pressed()
        if key[K_RIGHT]:
            grafo_0.mover_surf([-10,0])
            grafo_0.pintar_surf(ventana)
        elif key[K_LEFT]:
            grafo_0.mover_surf([10,0])
            grafo_0.pintar_surf(ventana)
        elif key[K_UP]:
            grafo_0.mover_surf([0,10])
            grafo_0.pintar_surf(ventana)
        elif key[K_DOWN]:
            grafo_0.mover_surf([0,-10])
            grafo_0.pintar_surf(ventana)
        elif key[K_w]:
            grafo_0.aumento([21,16])
            grafo_0.pintar_surf(ventana)
        elif key[K_s]:
            grafo_0.aumento([-21,-16])
            grafo_0.pintar_surf(ventana)
        pygame.display.update()
        timer.tick(20)

main()
