import numpy as np
import pygame
import pygame_menu
import sys

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
height = RANDURI * DIMENSIUNEBULINA + DIMENSIUNEBUTON
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
            pygame.draw.rect(screen,FUNDAL,(coloana*DIMENSIUNEBULINA,rand*DIMENSIUNEBULINA+DIMENSIUNEBULINA+DIMENSIUNEBUTON,DIMENSIUNEBULINA,DIMENSIUNEBULINA))
            pygame.draw.circle(screen,FUNDALBULINE,(int(coloana*DIMENSIUNEBULINA+DIMENSIUNEBULINA/2),int(rand*DIMENSIUNEBULINA+DIMENSIUNEBULINA+DIMENSIUNEBULINA/2+DIMENSIUNEBUTON)),RAZA)
    pygame.display.update()

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
    font = pygame.font.Font(None, 36)
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
    global pauza, tabla, meniuAfisat,popUpAfisat
    despre = ("Acesta este Connect 4.\n"
              "Un  joc  in  care  ai  ca  obiectiv  sa \n"
              "unesti  4  buline  intre  ele  pe  verticala,\n" 
              "orizontala sau pe diagonala.\n" 
              "Joc creat de Cazamir Andrei\n"
               "                    si Cirja Ioan.")
    tabla = creareTabla()
    pygame.init()
    menu = creeaza_meniu()
    while True:
        screen.fill(FUNDALSPATE)
        butonMeniu = deseneaza_buton_meniu()
        if popUpAfisat: 
            butonOK = deseneaza_popup(despre)
        elif meniuAfisat:
            menu.draw(screen)
            menu.update(pygame.event.get())
        else:
            if not pauza:
                deseneazaTabla(tabla)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                iesireJoc()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pozitieMouse = pygame.mouse.get_pos()
                if butonMeniu.collidepoint(pozitieMouse) and not meniuAfisat and not popUpAfisat:
                    meniuAfisat = True
                    pauza = True
                if popUpAfisat and butonOK.collidepoint(pozitieMouse):
                    popUpAfisat = False
                    meniuAfisat = True
        pygame.display.update()
        
if __name__=="__main__":
    main()