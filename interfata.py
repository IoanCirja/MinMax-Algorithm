import numpy as np
import random
import pygame
import sys
import math

FUNDAL = (60, 60, 60)
FUNDALBULINE = (200, 200, 200)
BULINEJUCATOR = (0, 255, 0)
BULINECALCULATOR = (255, 0, 0)

RANDURI = 8
COLOANE = 8
DIMENSIUNEBULINA = 75
RAZA = int(DIMENSIUNEBULINA / 2 - 10)

width = COLOANE * DIMENSIUNEBULINA
height = (RANDURI + 1) * DIMENSIUNEBULINA
size = (width, height)
screen = pygame.display.set_mode(size)


def creareTabla():
    return np.zeros((RANDURI, COLOANE))


def validLocatie(tabla, coloana):
    return tabla[RANDURI - 1][coloana] == 0


def urmRandLiber(tabla, coloana):
    for r in range(RANDURI):
        if tabla[r][coloana] == 0:
            return r
    return None 


def puneBulina(tabla, rand, coloana, bulina):
    tabla[rand][coloana] = bulina


def deseneazaTabla(tabla):
    for coloana in range(COLOANE):
        for rand in range(RANDURI):
            pygame.draw.rect(
                screen,
                FUNDAL,
                (
                    coloana * DIMENSIUNEBULINA,
                    rand * DIMENSIUNEBULINA + DIMENSIUNEBULINA,
                    DIMENSIUNEBULINA,
                    DIMENSIUNEBULINA,
                ),
            )
            pygame.draw.circle(
                screen,
                FUNDALBULINE,
                (
                    int(coloana * DIMENSIUNEBULINA + DIMENSIUNEBULINA / 2),
                    int(rand * DIMENSIUNEBULINA + DIMENSIUNEBULINA + DIMENSIUNEBULINA / 2),
                ),
                RAZA,
            )

    for coloana in range(COLOANE):
        for rand in range(RANDURI):
            if tabla[rand][coloana] == 1:
                pygame.draw.circle(
                    screen,
                    BULINEJUCATOR,
                    (
                        int(coloana * DIMENSIUNEBULINA + DIMENSIUNEBULINA / 2),
                        height
                        - int((rand + 1) * DIMENSIUNEBULINA - DIMENSIUNEBULINA / 2),
                    ),
                    RAZA,
                )
            elif tabla[rand][coloana] == 2:
                pygame.draw.circle(
                    screen,
                    BULINECALCULATOR,
                    (
                        int(coloana * DIMENSIUNEBULINA + DIMENSIUNEBULINA / 2),
                        height
                        - int((rand + 1) * DIMENSIUNEBULINA - DIMENSIUNEBULINA / 2),
                    ),
                    RAZA,
                )

    pygame.display.update()


def main():
    tabla = creareTabla()
    turn = random.randint(0, 1) 
    pygame.init()
    deseneazaTabla(tabla)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, FUNDAL, (0, 0, width, DIMENSIUNEBULINA))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(
                        screen, BULINEJUCATOR, (posx, int(DIMENSIUNEBULINA / 2)), RAZA
                    )

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, FUNDAL, (0, 0, width, DIMENSIUNEBULINA))


                posx = event.pos[0]
                coloana = int(math.floor(posx / DIMENSIUNEBULINA))

                if validLocatie(tabla, coloana):
                    rand = urmRandLiber(tabla, coloana)
                    puneBulina(tabla, rand, coloana, 1)

                    turn = 1 


                    coloana = random.randint(0, COLOANE - 1)

                    while not validLocatie(tabla, coloana):
                        coloana = random.randint(0, COLOANE - 1)

                pygame.time.wait(500)
                rand = urmRandLiber(tabla, coloana)
                puneBulina(tabla, rand, coloana, 2)

                turn = 0 

                deseneazaTabla(tabla)


if __name__ == "__main__":
    main()
