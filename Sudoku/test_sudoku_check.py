import unittest

import Sudoku.sudoku_check as sudoku

class TestSudoku(unittest.TestCase):

    def test_001_sudoku_check_string(self):
        self.assertFalse(sudoku.check_sudoku(
            [['a','b','c'],
            ['b','c','a'],
            ['c','a','b']]))

    def test_002_sudoku_check_float(self):
        self.assertFalse(sudoku.check_sudoku(
            [[1, 1.5],
             [1.5, 1]]))

    def test_003_sudoku_check_row(self):
        self.assertFalse(sudoku.check_sudoku(
            [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]))

    def test_004_sudoku_check_column(self):
        self.assertFalse(sudoku.check_sudoku(
            [[1, 2, 3, 4],
             [2, 3, 1, 4],
             [4, 1, 2, 3],
             [3, 4, 1, 2]]))

    def test_005_sudoku_check_greater_number(self):
        self.assertFalse(sudoku.check_sudoku(
            [[1, 2, 3, 4, 5],
             [2, 3, 1, 5, 6],
             [4, 5, 2, 1, 3],
             [3, 4, 5, 2, 1],
             [5, 6, 4, 3, 2]]))

    def test_006_sudoku_check_negative_number(self):
        self.assertFalse(sudoku.check_sudoku(
            [[-1, -2, -3, -4, -5],
             [-2, -3, -1, -5, -6],
             [-4, -5, -2, -1, -3],
             [-3, -4, -5, -2, -1],
             [-5, -6, -4, -3, -2]]))

    def test_007_sudoku_check_zero(self):
        self.assertFalse(sudoku.check_sudoku(
            [[1, 2, 0],
             [2, 0, 1],
             [0, 1, 2]]))

    def test_008_sudoku_check_correct1(self):
        self.assertTrue(sudoku.check_sudoku(
            [[1, 2, 3],
             [2, 3, 1],
             [3, 1, 2]]))

    def test_009_sudoku_check_correct2(self):
        self.assertTrue(sudoku.check_sudoku(
            [[1, 2, 3, 4, 5],
             [2, 3, 4, 5, 1],
             [3, 4, 5, 1, 2],
             [4, 5, 1, 2, 3],
             [5, 1, 2, 3, 4]]))
