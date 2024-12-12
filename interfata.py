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
pygame.init()

font = pygame.font.SysFont("monospace", 30)

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


def checkWin(tabla, piece):
    for r in range(RANDURI):
        for c in range(COLOANE - 3):
            if (
                tabla[r][c] == piece
                and tabla[r][c + 1] == piece
                and tabla[r][c + 2] == piece
                and tabla[r][c + 3] == piece
            ):
                return True

    for c in range(COLOANE):
        for r in range(RANDURI - 3):
            if (
                tabla[r][c] == piece
                and tabla[r + 1][c] == piece
                and tabla[r + 2][c] == piece
                and tabla[r + 3][c] == piece
            ):
                return True

    for r in range(RANDURI - 3):
        for c in range(COLOANE - 3):
            if (
                tabla[r][c] == piece
                and tabla[r + 1][c + 1] == piece
                and tabla[r + 2][c + 2] == piece
                and tabla[r + 3][c + 3] == piece
            ):
                return True

    for r in range(3, RANDURI):
        for c in range(COLOANE - 3):
            if (
                tabla[r][c] == piece
                and tabla[r - 1][c + 1] == piece
                and tabla[r - 2][c + 2] == piece
                and tabla[r - 3][c + 3] == piece
            ):
                return True

    return False


def showWinner(winner):
    popup_width, popup_height = 400, 200
    popup_x = (width - popup_width) // 2
    popup_y = (height - popup_height) // 2

    popup_surface = pygame.Surface((popup_width, popup_height))
    popup_surface.fill((30, 30, 30))

    pygame.draw.rect(popup_surface, (255, 255, 255), (0, 0, popup_width, popup_height), 5)

    if winner == 1:
        label = font.render("Player Wins!", True, BULINEJUCATOR)
    else:
        label = font.render("Computer Wins!", True, BULINECALCULATOR)

    label_x = (popup_width - label.get_width()) // 2
    label_y = (popup_height - label.get_height()) // 2
    popup_surface.blit(label, (label_x, label_y))

    screen.blit(popup_surface, (popup_x, popup_y))
    pygame.display.update()
    pygame.time.wait(3000)
    sys.exit()



def main():
    tabla = creareTabla()
    turn = random.randint(0, 1)

    deseneazaTabla(tabla)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if turn == 0:  
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, FUNDAL, (0, 0, width, DIMENSIUNEBULINA))
                    posx = event.pos[0]
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

                        if checkWin(tabla, 1):
                            game_over = True
                            showWinner(1)

                        turn = 1
                        deseneazaTabla(tabla)

        if turn == 1 and not game_over:
            pygame.time.wait(500)
            coloana = random.randint(0, COLOANE - 1)

            while not validLocatie(tabla, coloana):
                coloana = random.randint(0, COLOANE - 1)

            rand = urmRandLiber(tabla, coloana)
            puneBulina(tabla, rand, coloana, 2)

            if checkWin(tabla, 2):
                game_over = True
                showWinner(2)

            turn = 0
            deseneazaTabla(tabla)


if __name__ == "__main__":
    main()
