import numpy as np
import pygame
import pygame_menu
import sys
import math
import random

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
height = (RANDURI + 3) * DIMENSIUNEBULINA
size = (width,height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")
screen.fill(FUNDALSPATE)

tabla = None
pauza =  False
meniuAfisat = False
popUpAfisat = False

def creareTabla():
    return np.zeros((RANDURI,COLOANE)) 

def deseneazaTabla(tabla):
    for coloana in range(COLOANE):
        for rand in range(RANDURI):
            pygame.draw.rect(
                screen,
                FUNDAL,
                (
                    coloana * DIMENSIUNEBULINA,
                    (rand + 2)* DIMENSIUNEBULINA + DIMENSIUNEBULINA,
                    DIMENSIUNEBULINA,
                    DIMENSIUNEBULINA,
                ),
            )
            pygame.draw.circle(
                screen,
                FUNDALBULINE,
                (
                    int(coloana * DIMENSIUNEBULINA + DIMENSIUNEBULINA / 2),
                    int((rand +2) * DIMENSIUNEBULINA + DIMENSIUNEBULINA + DIMENSIUNEBULINA / 2),
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

    pygame.display.flip()

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

def validLocatie(tabla, coloana):
    return tabla[RANDURI - 1][coloana] == 0


def urmRandLiber(tabla, coloana):
    for r in range(RANDURI):
        if tabla[r][coloana] == 0:
            return r
    return None


def puneBulina(tabla, rand, coloana, bulina):
    tabla[rand][coloana] = bulina


def showWinner(winner):
    popup_width, popup_height = 400, 200
    popup_x = (width - popup_width) // 2
    popup_y = (height - popup_height) // 2

    popup_surface = pygame.Surface((popup_width, popup_height))
    popup_surface.fill((30, 30, 30))

    pygame.draw.rect(popup_surface, (255, 255, 255), (0, 0, popup_width, popup_height), 5)
    font = pygame.font.Font(None, 36)

    if winner == 1:
        label = font.render("Player Wins!", True, BULINEJUCATOR)
    else:
        label = font.render("Computer Wins!", True, BULINECALCULATOR)

    label_x = (popup_width - label.get_width()) // 2
    label_y = (popup_height - label.get_height()) // 2
    popup_surface.blit(label, (label_x, label_y))

    screen.blit(popup_surface, (popup_x, popup_y))
    pygame.display.flip()
    pygame.time.wait(3000)
    sys.exit()


def startJoc():
    print("Start joc")
    global pauza, tabla, meniuAfisat, popUpAfisat
    pauza = False
    meniuAfisat = False
    popUpAfisat = False

def startJocNou():
    print("Start joc nou")
    global pauza, tabla, meniuAfisat, popUpAfisat
    pauza = False
    tabla = creareTabla()
    meniuAfisat = False
    popUpAfisat = False

def despreJoc():
    print("Despre joc")
    global popUpAfisat
    popUpAfisat = True

def iesireJoc():
    pygame.quit()
    sys.exit()

def creeaza_meniu():
    menu = pygame_menu.Menu('Meniu principal', width, height,
                            theme=pygame_menu.themes.THEME_DEFAULT)
    menu.add.button('Revenire', startJoc)
    menu.add.button('Joc Nou', startJocNou)
    menu.add.button('Despre', despreJoc)
    menu.add.button('Ieșire', iesireJoc)
    return menu

def deseneaza_buton_meniu():
    buton_rect = pygame.Rect(0, 0, 100, DIMENSIUNEBUTON)
    pygame.draw.rect(screen, FUNDAL, buton_rect)
    font = pygame.font.SysFont("monospace", 30)
    text = font.render("Meniu", True, (255, 255, 255))
    screen.blit(text, (buton_rect.x + (buton_rect.width - text.get_width()) // 2, 
                       buton_rect.y + (buton_rect.height - text.get_height()) // 2))
    return buton_rect

def deseneaza_popup(mesaj):
    latime_popup = 500
    inaltime_popup = 350
    popup_rect = pygame.Rect((width - latime_popup) // 2, (height - inaltime_popup) // 2, latime_popup, inaltime_popup)
    pygame.draw.rect(screen, (0, 0, 0), popup_rect)
    pygame.draw.rect(screen, (255, 255, 255), popup_rect, 5)

    font = pygame.font.Font(None, 36)
    mesaj_linii = mesaj.split("\n")
    text_x = popup_rect.x + 20
    text_y = popup_rect.y + 20
    for linie in mesaj_linii:
        text_surface = font.render(linie, True, (255, 255, 255))
        screen.blit(text_surface, (text_x, text_y))
        text_y += 40

    buton_ok = pygame.Rect(popup_rect.x + (popup_rect.width - 100) // 2, popup_rect.y + popup_rect.height - 50, 100, 40)
    pygame.draw.rect(screen, (0, 255, 0), buton_ok)
    buton_font = pygame.font.Font(None, 30)
    buton_text = buton_font.render("OK", True, (0, 0, 0))
    screen.blit(buton_text, (buton_ok.x + (buton_ok.width - buton_text.get_width()) // 2,
                             buton_ok.y + (buton_ok.height - buton_text.get_height()) // 2))

    return buton_ok

def main():
    global pauza, tabla, meniuAfisat, popUpAfisat
    despre = ("Acesta este Connect 4.\n"
              "Un joc in care ai ca obiectiv sa\n"
              "unesti 4 buline intre ele pe verticala,\n" 
              "orizontala sau pe diagonala.\n" 
              "Joc creat de Cazamir Andrei\n"
              "si Cirja Ioan.")
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

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()