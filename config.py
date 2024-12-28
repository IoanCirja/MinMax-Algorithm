import pygame

FUNDAL = (60,60,60)
FUNDALBULINE = (200,200,200)
BULINEJUCATOR = (0,255,0)
BULINECALCULATOR = (255,0,0)
FUNDALSPATE = (180,180,180)

RANDURI = 8
COLOANE = 8
DIMENSIUNEBULINA = 75
RAZA = int(DIMENSIUNEBULINA/2-10)

DIMENSIUNEBUTON = 35

width = COLOANE * DIMENSIUNEBULINA
height = (RANDURI + 2) * DIMENSIUNEBULINA
size = (width,height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")
screen.fill(FUNDALSPATE)

tabla = None
pauza =  False
meniuAfisat = False
popUpAfisat = False