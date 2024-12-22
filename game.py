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
    global pauza, tabla, meniuAfisat, popUpAfisat
    tabla = creareTabla()
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()

    turn = random.randint(0, 1)
    game_over = False

    menu = creeaza_meniu()

    player_ball_surface = pygame.Surface((width, DIMENSIUNEBULINA))
    player_ball_surface.set_colorkey((0, 0, 0))

    mouse_x = None

    while True:
        screen.fill(FUNDALSPATE)
        butonMeniu = deseneaza_buton_meniu()

        if popUpAfisat:
            butonOK = deseneaza_popup(despre)
        elif meniuAfisat:
            menu.draw(screen)
            menu.flip(pygame.event.get())
        else:
            if not pauza:
                deseneazaTabla(tabla)

        if mouse_x is not None:
            pygame.draw.circle(
                screen, BULINEJUCATOR, (mouse_x, 4 * int(DIMENSIUNEBULINA / 2)), RAZA
            )
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                iesireJoc()

            if meniuAfisat or popUpAfisat:
                if popUpAfisat and event.type == pygame.MOUSEBUTTONDOWN:
                    pozitieMouse = pygame.mouse.get_pos()
                    if butonOK.collidepoint(pozitieMouse):
                        popUpAfisat = False
                        meniuAfisat = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pozitieMouse = pygame.mouse.get_pos()
                    if butonMeniu.collidepoint(pozitieMouse):
                        meniuAfisat = False
                        pauza = False
            else:
                if turn == 0 and not pauza:
                    if event.type == pygame.MOUSEMOTION:
                        mouse_x = event.pos[0]

                    pygame.display.flip()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pozitieMouse = pygame.mouse.get_pos()
                    if butonMeniu.collidepoint(pozitieMouse):
                        meniuAfisat = True
                        pauza = True

                    if turn == 0 and not pauza:
                        pygame.draw.rect(screen, FUNDALSPATE, (0, 0, width, DIMENSIUNEBULINA))
                        posx = event.pos[0]
                        coloana = int(math.floor(posx / DIMENSIUNEBULINA))

                        if validLocatie(tabla, coloana):
                            rand = urmRandLiber(tabla, coloana)
                            puneBulina(tabla, rand, coloana, 1)

                            if checkWin(tabla, 1):
                                game_over = True
                                showWinner(1)

                            turn = 1
                            deseneazaTabla(tabla)

                if turn == 1 and not game_over and not pauza:
                    pygame.time.wait(500)
                    coloana = aiMove(tabla)

                    rand = urmRandLiber(tabla, coloana)
                    puneBulina(tabla, rand, coloana, 2)

                    if checkWin(tabla, 2):
                        game_over = True
                        showWinner(2)

                    turn = 0
                    deseneazaTabla(tabla)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()