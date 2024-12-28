import pygame
import pygame_menu
from config import *
from tabla import *

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