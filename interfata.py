import numpy as np
import random
import pygame
import sys
import math

FUNDAL = (60,60,60)
FUNDALBULINE = (200,200,200)
BULINEJUCATOR = (0,255,0)
BULINECALCULATOR = (255,0,0)

RANDURI = 8
COLOANE = 8
DIMENSIUNEBULINA = 75
RAZA = int(DIMENSIUNEBULINA/2-10)

width = COLOANE * DIMENSIUNEBULINA
height = RANDURI * DIMENSIUNEBULINA
size = (width,height)
screen = pygame.display.set_mode(size)

def creareTabla():
    tabla = np.zeros((RANDURI,COLOANE))

def afiseazaTabla(tabla):
    print(np.flip(tabla,0))

def deseneazaTabla(tabla):
    for coloana in range(COLOANE):
        for rand in range(RANDURI):
            pygame.draw.rect(screen,FUNDAL,(coloana*DIMENSIUNEBULINA,rand*DIMENSIUNEBULINA+DIMENSIUNEBULINA,DIMENSIUNEBULINA,DIMENSIUNEBULINA))
            pygame.draw.circle(screen,FUNDALBULINE,(int(coloana*DIMENSIUNEBULINA+DIMENSIUNEBULINA/2),int(rand*DIMENSIUNEBULINA+DIMENSIUNEBULINA+DIMENSIUNEBULINA/2)),RAZA)
    pygame.display.update()

def main():
    tabla = creareTabla()
    #afiseazaTabla(tabla)
    pygame.init()
    deseneazaTabla(tabla)
    pygame.display.update()
    pygame.time.wait(50000)

if __name__=="__main__":
    main()