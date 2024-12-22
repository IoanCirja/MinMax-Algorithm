from config import *
import numpy as np

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
