import numpy as np
import pygame
import pygame_menu
import sys
import math
import random
from config import *
from tabla import *
from meniu import *

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
    return buton_ok

def minimax(tabla, depth, alpha, beta, is_maximizing, piece):
    valid_moves = getValidMoves(tabla)
    if depth == 0 or not valid_moves:
        return evaluate(tabla, piece)
    
    if is_maximizing:
        max_eval = -math.inf
        for move in valid_moves:
            row = urmRandLiber(tabla, move)
            makeMove(tabla, row, move, piece)
            eval = minimax(tabla, depth-1, alpha, beta, False, piece)
            undoMove(tabla, row, move)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in valid_moves:
            row = urmRandLiber(tabla, move)
            makeMove(tabla, row, move, 3 - piece)
            eval = minimax(tabla, depth-1, alpha, beta, True, piece)
            undoMove(tabla, row, move)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def getValidMoves(tabla):
    return [c for c in range(COLOANE) if validLocatie(tabla, c)]

def evaluate(tabla, piece):
    score = 0
    for r in range(RANDURI):
        for c in range(COLOANE - 3):
            score += scorePosition(tabla, r, c, 1, 0, piece)
            score += scorePosition(tabla, r, c, 0, 1, piece)
            score += scorePosition(tabla, r, c, 1, 1, piece)
            score += scorePosition(tabla, r, c, 1, -1, piece)
    return score

def scorePosition(tabla, r, c, dr, dc, piece):
    count = 0
    for i in range(4):
        if r + i*dr < 0 or r + i*dr >= RANDURI or c + i*dc < 0 or c + i*dc >= COLOANE:
            return 0
        if tabla[r + i*dr][c + i*dc] == piece:
            count += 1
        elif tabla[r + i*dr][c + i*dc] != 0:
            return 0
    return count

def makeMove(tabla, row, col, piece):
    tabla[row][col] = piece

def undoMove(tabla, row, col):
    tabla[row][col] = 0

def aiMove(tabla):
    best_score = -math.inf
    best_moves = []

    for move in getValidMoves(tabla):
        row = urmRandLiber(tabla, move)
        makeMove(tabla, row, move, 2)
        score = minimax(tabla, 4, -math.inf, math.inf, False, 2)
        undoMove(tabla, row, move)

        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)

    return random.choice(best_moves)
