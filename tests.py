import unittest
import numpy as np
from unittest.mock import patch
from config import *
from tabla import *
from meniu import *
from algoritm import *

BULINE_JUCATOR = 1
BULINE_CALCULATOR = 2
class TestGameFunctions(unittest.TestCase):

    def setUp(self):
        """Set up an empty board for testing."""
        self.tabla = np.zeros((RANDURI, COLOANE), dtype=int)

    

    def test_checkWin_horizontal(self):
        """Test horizontal win."""
        for i in range(4):
            self.tabla[0][i] = BULINE_JUCATOR
        self.assertTrue(checkWin(self.tabla, BULINE_JUCATOR))

    def test_checkWin_vertical(self):
        """Test vertical win."""
        for i in range(4):
            self.tabla[i][0] = BULINE_JUCATOR
        self.assertTrue(checkWin(self.tabla, BULINE_JUCATOR))

    def test_checkWin_diagonal_positive(self):
        """Test positive slope diagonal win."""
        for i in range(4):
            self.tabla[i][i] = BULINE_JUCATOR
        self.assertTrue(checkWin(self.tabla, BULINE_JUCATOR))

    def test_checkWin_diagonal_negative(self):
        """Test negative slope diagonal win."""
        for i in range(4):
            self.tabla[i][3 - i] = BULINE_JUCATOR
        self.assertTrue(checkWin(self.tabla, BULINE_JUCATOR))

    def test_checkWin_no_win(self):
        """Test that no win is detected on an empty board."""
        self.assertFalse(checkWin(self.tabla, BULINE_JUCATOR))

    def test_validLocatie(self):
        """Test if a column is a valid location."""
        self.assertTrue(validLocatie(self.tabla, 0))
        self.tabla[RANDURI - 1][0] = BULINE_JUCATOR
        self.assertFalse(validLocatie(self.tabla, 0))

    def test_urmRandLiber(self):
        """Test finding the next free row in a column."""
        self.assertEqual(urmRandLiber(self.tabla, 0), 0)
        self.tabla[0][0] = BULINE_JUCATOR
        self.assertEqual(urmRandLiber(self.tabla, 0), 1)

    def test_puneBulina(self):
        """Test placing a piece on the board."""
        puneBulina(self.tabla, 0, 0, BULINE_JUCATOR)
        self.assertEqual(self.tabla[0][0], BULINE_JUCATOR)

    def test_getValidMoves(self):
        """Test retrieving valid moves."""
        valid_moves = getValidMoves(self.tabla)
        self.assertEqual(valid_moves, list(range(COLOANE)))
        for c in range(COLOANE):
            self.tabla[RANDURI - 1][c] = BULINE_JUCATOR
        self.assertEqual(getValidMoves(self.tabla), [])

    def test_aiMove(self):
        """Test AI move generation."""
        for i in range(3):
            self.tabla[i][0] = BULINE_CALCULATOR
        move = aiMove(self.tabla)
        self.assertEqual(move, 0)

    def test_make_undo_move(self):
        """Test making and undoing a move."""
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
        """Test if the board is created correctly with all zeros."""
        tabla = creareTabla()
        self.assertEqual(tabla.shape, (8, 8))  
        self.assertTrue(np.all(tabla == 0))    

    def test_valid_locatie(self):
        """Test if a column is valid for a new piece."""
        tabla = creareTabla()
        self.assertTrue(validLocatie(tabla, 0))  
        tabla[7][0] = 1  
        self.assertFalse(validLocatie(tabla, 0))  

    def test_urm_rand_liber(self):
        """Test finding the first available row in a column."""
        tabla = creareTabla()
        self.assertEqual(urmRandLiber(tabla, 0), 0)  
        tabla[0][0] = 1  
        self.assertEqual(urmRandLiber(tabla, 0), 1)  

    def test_pune_bulina(self):
        """Test placing a piece on the board."""
        tabla = creareTabla()
        puneBulina(tabla, 0, 0, 1)  
        self.assertEqual(tabla[0][0], 1)  
        puneBulina(tabla, 1, 1, 2)  
        self.assertEqual(tabla[1][1], 2)  

    def test_check_win_horizontal(self):
        """Test horizontal win condition."""
        tabla = creareTabla()
        for c in range(4):  
            puneBulina(tabla, 0, c, 1)
        self.assertTrue(checkWin(tabla, 1))  

    def test_check_win_vertical(self):
        """Test vertical win condition."""
        tabla = creareTabla()
        for r in range(4):  
            puneBulina(tabla, r, 0, 1)
        self.assertTrue(checkWin(tabla, 1))  

    def test_check_win_diagonal_positive(self):
        """Test diagonal win condition (positive slope)."""
        tabla = creareTabla()
        puneBulina(tabla, 3, 0, 1)
        puneBulina(tabla, 2, 1, 1)
        puneBulina(tabla, 1, 2, 1)
        puneBulina(tabla, 0, 3, 1)
        self.assertTrue(checkWin(tabla, 1))  

    def test_check_win_diagonal_negative(self):
        """Test diagonal win condition (negative slope)."""
        tabla = creareTabla()
        puneBulina(tabla, 0, 0, 1)
        puneBulina(tabla, 1, 1, 1)
        puneBulina(tabla, 2, 2, 1)
        puneBulina(tabla, 3, 3, 1)
        self.assertTrue(checkWin(tabla, 1))  

    def test_no_win(self):
        """Test no win condition."""
        tabla = creareTabla()
        puneBulina(tabla, 0, 0, 1)
        puneBulina(tabla, 0, 1, 1)
        puneBulina(tabla, 0, 2, 1)
        self.assertFalse(checkWin(tabla, 1))  

if __name__ == "__main__":
    unittest.main()
