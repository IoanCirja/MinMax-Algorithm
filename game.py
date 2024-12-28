import numpy as np
import pygame
import pygame_menu
import sys
import math
import random
from config import *
from tabla import *
from meniu import *
from algoritm import *

def main():
    tabla = config.tabla = creareTabla()
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    despre = ("Acesta este Connect 4.\n"
              "Un joc in care ai ca obiectiv sa\n"
              "unesti 4 buline intre ele pe verticala,\n" 
              "orizontala sau pe diagonala.\n" 
              "Joc creat de Cazamir Andrei\n"
              "si Cirja Ioan.")
    
    turn = random.randint(0, 1)
    menu = creeaza_meniu()
    start = creeaza_meniu_start()
    level = creeaza_pagina_niveluri()
    player_ball_surface = pygame.Surface((width, DIMENSIUNEBULINA))
    player_ball_surface.set_colorkey((0, 0, 0))
    mouse_x = None
    pauza = config.pauza
    meniuAfisat = config.meniuAfisat
    popUpAfisat = config.popUpAfisat
    while True:
        gameOver = config.gameOver
        tabla = config.tabla
        pauza = config.pauza
        meniuAfisat = config.meniuAfisat
        popUpAfisat = config.popUpAfisat
        startAfisat = config.startAfisat
        alegereAfisat = config.alegereAfisat
        screen.fill(FUNDALSPATE)
        butonMeniu = deseneaza_buton_meniu()
        
        if alegereAfisat:
            level.draw(screen)
            level.update(pygame.event.get())
        if popUpAfisat:
            butonOK = deseneaza_popup(despre)
        elif meniuAfisat:
            menu.draw(screen)
            menu.update(pygame.event.get())
        elif startAfisat:
            start.draw(screen)
            start.update(pygame.event.get())
        else:
            if not pauza:
                deseneazaTabla(tabla)
                if mouse_x is not None:
                    pygame.draw.circle(
                        screen, BULINEJUCATOR, (mouse_x,  int(2.75 * DIMENSIUNEBULINA / 2)), RAZA
                    )
                    pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                iesireJoc()
            
            if turn == 0 and not pauza:
                if event.type == pygame.MOUSEMOTION:
                    mouse_x = event.pos[0]
                pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pozitieMouse = pygame.mouse.get_pos()
                if butonMeniu.collidepoint(pozitieMouse):
                    meniuAfisat = True
                    config.meniuAfisat = True
                    pauza = True
                    config.pauza = True
                if not startAfisat and popUpAfisat and butonOK.collidepoint(pozitieMouse):
                    popUpAfisat = False
                    config.popUpAfisat = False
                    meniuAfisat =  True
                    config.meniuAfisat = True
                elif  startAfisat and popUpAfisat and butonOK.collidepoint(pozitieMouse):
                    popUpAfisat = False
                    config.popUpAfisat = False

                if turn == 0 and not pauza:
                    pygame.draw.rect(screen, FUNDALSPATE, (0, 0, width, DIMENSIUNEBULINA))
                    posx = event.pos[0]
                    coloana = int(math.floor(posx / DIMENSIUNEBULINA))

                    if validLocatie(tabla, coloana):
                        rand = urmRandLiber(tabla, coloana)
                        puneBulina(tabla, rand, coloana, 1)
                        turn = 1
                        deseneazaTabla(tabla)
                        if checkWin(tabla, 1):
                            gameOver = True
                            showWinner(1)            

            if turn == 1 and not gameOver and not pauza:
                pygame.time.wait(500)
                coloana = aiMove(tabla)
                rand = urmRandLiber(tabla, coloana)
                puneBulina(tabla, rand, coloana, 2)
                turn = 0
                deseneazaTabla(tabla)
                if checkWin(tabla, 2):
                    gameOver = True
                    showWinner(2)

        pygame.display.flip()
        clock.tick(60)
       
        
if __name__ == "__main__":
    main()