import config
from config import *
import numpy as np
import sys

def startJoc():
    print("Start joc")
    config.pauza = False
    config.meniuAfisat = False
    config.popUpAfisat = False
    config.startAfisat = False

def alegereNumar():
    config.pauza = True
    config.alegereAfisat = True
    config.niveluri = 3
    config.meniuAfisat = False
    config.popUpAfisat = False
    config.startAfisat = False

def startJocNou(nivel):
    print("Start joc nou")
    config.pauza = False
    config.tabla = creareTabla()
    config.meniuAfisat = False
    config.popUpAfisat = False
    config.startAfisat = False
    config.alegereAfisat = False
    config.levels = nivel
    
def despreJoc():
    print("Despre joc")
    config.popUpAfisat = True

def iesireJoc():
    pygame.quit()
    sys.exit()

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
                    (rand + 1)* DIMENSIUNEBULINA + DIMENSIUNEBULINA,
                    DIMENSIUNEBULINA,
                    DIMENSIUNEBULINA,
                ),
            )
            pygame.draw.circle(
                screen,
                FUNDALBULINE,
                (
                    int(coloana * DIMENSIUNEBULINA + DIMENSIUNEBULINA / 2),
                    int((rand + 1) * DIMENSIUNEBULINA + DIMENSIUNEBULINA + DIMENSIUNEBULINA / 2),
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
