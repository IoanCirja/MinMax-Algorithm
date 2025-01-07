import unittest
import numpy as np
from unittest.mock import patch, MagicMock
from config import *
from tabla import *
from meniu import *
from algoritm import *

BULINE_JUCATOR = 1
BULINE_CALCULATOR = 2
class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        self.tabla = np.zeros((RANDURI, COLOANE), dtype=int)



    def test_evaluate_center_column(self):
        self.tabla[:, COLOANE // 2] = [BULINE_JUCATOR] * RANDURI
        score = evaluate(self.tabla, BULINE_JUCATOR)
        self.assertGreater(score, 0)


    def test_evaluate_mixed_board(self):
        self.tabla[0, :4] = BULINE_JUCATOR
        self.tabla[1, :4] = BULINE_CALCULATOR
        score = evaluate(self.tabla, BULINE_JUCATOR)
        self.assertGreater(score, 0)





    def test_scoreWindow(self):
        window = [BULINE_JUCATOR, BULINE_JUCATOR, BULINE_JUCATOR, 0]
        self.assertEqual(scoreWindow(window, BULINE_JUCATOR), 10)
        
        window = [BULINE_JUCATOR, BULINE_JUCATOR, 0, 0]
        self.assertEqual(scoreWindow(window, BULINE_JUCATOR), 5)
        
        window = [BULINE_CALCULATOR, BULINE_CALCULATOR, BULINE_CALCULATOR, 0]
        self.assertEqual(scoreWindow(window, BULINE_CALCULATOR), 10)
        
        window = [BULINE_CALCULATOR, BULINE_JUCATOR, 0, BULINE_CALCULATOR]
        self.assertEqual(scoreWindow(window, BULINE_CALCULATOR), 0)

    def test_aiMove_defensive(self):
        
        for i in range(3):
            self.tabla[i][0] = BULINE_JUCATOR
        move = aiMove(self.tabla)
        self.assertEqual(move, 0)  

    def test_aiMove_offensive(self):
        
        for i in range(3):
            self.tabla[i][0] = BULINE_CALCULATOR
        move = aiMove(self.tabla)
        self.assertEqual(move, 0)  

    def test_aiMove_tiebreak(self):
        
        move = aiMove(self.tabla)
        self.assertIn(move, range(COLOANE))

    def test_minimax_depth_limit(self):
        
        config.levels = 2  
        score = minimax(self.tabla, 0, -float('inf'), float('inf'), True, BULINE_CALCULATOR)
        self.assertIsInstance(score, (int, float))

    def test_getValidMoves_full_board(self):
        
        self.tabla[:, :] = BULINE_JUCATOR
        valid_moves = getValidMoves(self.tabla)
        self.assertEqual(valid_moves, [])  

    def test_getValidMoves_partial_board(self):
        
        self.tabla[RANDURI - 1, :] = BULINE_JUCATOR
        self.tabla[RANDURI - 1, 3] = 0  
        valid_moves = getValidMoves(self.tabla)
        self.assertEqual(valid_moves, [3])  


    def test_checkWin_horizontal(self):
        for i in range(4):
            self.tabla[0][i] = BULINE_JUCATOR
        self.assertTrue(checkWin(self.tabla, BULINE_JUCATOR))

    def test_checkWin_vertical(self):
        for i in range(4):
            self.tabla[i][0] = BULINE_JUCATOR
        self.assertTrue(checkWin(self.tabla, BULINE_JUCATOR))

    def test_checkWin_diagonal_positive(self):
        for i in range(4):
            self.tabla[i][i] = BULINE_JUCATOR
        self.assertTrue(checkWin(self.tabla, BULINE_JUCATOR))

    def test_checkWin_diagonal_negative(self):
        for i in range(4):
            self.tabla[i][3 - i] = BULINE_JUCATOR
        self.assertTrue(checkWin(self.tabla, BULINE_JUCATOR))

    def test_checkWin_no_win(self):
        self.assertFalse(checkWin(self.tabla, BULINE_JUCATOR))

    def test_validLocatie(self):
        self.assertTrue(validLocatie(self.tabla, 0))
        self.tabla[RANDURI - 1][0] = BULINE_JUCATOR
        self.assertFalse(validLocatie(self.tabla, 0))

    def test_urmRandLiber(self):
        self.assertEqual(urmRandLiber(self.tabla, 0), 0)
        self.tabla[0][0] = BULINE_JUCATOR
        self.assertEqual(urmRandLiber(self.tabla, 0), 1)

    def test_puneBulina(self):
        puneBulina(self.tabla, 0, 0, BULINE_JUCATOR)
        self.assertEqual(self.tabla[0][0], BULINE_JUCATOR)

    def test_getValidMoves(self):
        valid_moves = getValidMoves(self.tabla)
        self.assertEqual(valid_moves, list(range(COLOANE)))
        for c in range(COLOANE):
            self.tabla[RANDURI - 1][c] = BULINE_JUCATOR
        self.assertEqual(getValidMoves(self.tabla), [])

    def test_aiMove(self):
        for i in range(3):
            self.tabla[i][0] = BULINE_CALCULATOR
        move = aiMove(self.tabla)
        self.assertEqual(move, 0)

    def test_make_undo_move(self):
        makeMove(self.tabla, 0, 0, BULINE_JUCATOR)
        self.assertEqual(self.tabla[0][0], BULINE_JUCATOR)
        undoMove(self.tabla, 0, 0)
        self.assertEqual(self.tabla[0][0], 0)

        board = self.tabla.copy()
        for i in range(3):
            board[0][i] = 2
        move = aiMove(board)
        self.assertEqual(move, 3)

    def test_minimax(self):
        board = self.tabla.copy()
        for i in range(3):
            board[0][i] = 1
        score = minimax(board, 0, -float('inf'), float('inf'), True, 1)
        self.assertTrue(score > 0)

    def test_evaluate(self):
        board = self.tabla.copy()
        board[0][0:4] = 1
        score = evaluate(board, 1)
        self.assertTrue(score > 0)

 
    def test_creare_tabla(self):
        tabla = creareTabla()
        self.assertEqual(tabla.shape, (8, 8))  
        self.assertTrue(np.all(tabla == 0))    

    def test_valid_locatie(self):
        tabla = creareTabla()
        self.assertTrue(validLocatie(tabla, 0))  
        tabla[7][0] = 1  
        self.assertFalse(validLocatie(tabla, 0))  

    def test_urm_rand_liber(self):
        tabla = creareTabla()
        self.assertEqual(urmRandLiber(tabla, 0), 0)  
        tabla[0][0] = 1  
        self.assertEqual(urmRandLiber(tabla, 0), 1)  

    def test_pune_bulina(self):
        tabla = creareTabla()
        puneBulina(tabla, 0, 0, 1)  
        self.assertEqual(tabla[0][0], 1)  
        puneBulina(tabla, 1, 1, 2)  
        self.assertEqual(tabla[1][1], 2)  

    def test_check_win_horizontal(self):
        tabla = creareTabla()
        for c in range(4):  
            puneBulina(tabla, 0, c, 1)
        self.assertTrue(checkWin(tabla, 1))  

    def test_check_win_vertical(self):
        tabla = creareTabla()
        for r in range(4):  
            puneBulina(tabla, r, 0, 1)
        self.assertTrue(checkWin(tabla, 1))  

    def test_check_win_diagonal_positive(self):
        tabla = creareTabla()
        puneBulina(tabla, 3, 0, 1)
        puneBulina(tabla, 2, 1, 1)
        puneBulina(tabla, 1, 2, 1)
        puneBulina(tabla, 0, 3, 1)
        self.assertTrue(checkWin(tabla, 1))  

    def test_check_win_diagonal_negative(self):
        tabla = creareTabla()
        puneBulina(tabla, 0, 0, 1)
        puneBulina(tabla, 1, 1, 1)
        puneBulina(tabla, 2, 2, 1)
        puneBulina(tabla, 3, 3, 1)
        self.assertTrue(checkWin(tabla, 1))  

    def test_no_win(self):
        tabla = creareTabla()
        puneBulina(tabla, 0, 0, 1)
        puneBulina(tabla, 0, 1, 1)
        puneBulina(tabla, 0, 2, 1)
        self.assertFalse(checkWin(tabla, 1))  

if __name__ == "__main__":
    unittest.main()
