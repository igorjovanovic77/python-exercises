import unittest

import Identity_matrix.identity_matrix as identity_mtx

class TestIdentity_matrix(unittest.TestCase):

    def test_001_4x4_true(self):
        self.assertTrue(identity_mtx.is_identity_matrix(
            [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]))

    def test_002_3x3_false_0_instead_of_1(self):
        self.assertFalse(identity_mtx.is_identity_matrix(
            [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]))

    def test_003_3x3_false_2_instead_of_1(self):
        self.assertFalse(identity_mtx.is_identity_matrix(
            [[2, 0, 0],
            [0, 2, 0],
            [0, 0, 2]]))

    def test_004_3x4_false(self):
        self.assertFalse(identity_mtx.is_identity_matrix(
            [[1, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 1]]))

    def test_005_1x9_false(self):
        self.assertFalse(identity_mtx.is_identity_matrix(
            [[1, 0, 0, 0, 0, 0, 0, 0, 0]]))

    def test_006_4x4_false_1_instead_of_0(self):
        self.assertFalse(identity_mtx.is_identity_matrix(
            [[1, 0, 0, 0],
             [0, 1, 0, 1],
             [0, 0, 1, 0],
             [0, 0, 0, 1]]))

    def test_007_3x3_false_negative_1_instead_of_0(self):
        self.assertFalse(identity_mtx.is_identity_matrix(
            [[1, -1, 1],
             [0, 1, 0],
             [0, 0, 1]]))
