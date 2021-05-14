import unittest
from functions import get_number_from_index, get_empty_list, get_index_from_number, is_there_an_empty_cell, \
move_left, move_up, move_down, is_there_a_way_out

class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1,2),7)

    def test_2(self):
        self.assertEqual(get_number_from_index(3,3),16)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        l = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(l),a)

    def test_4(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        l = [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(l), a)

    def test_5(self):
        a = []
        l = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(get_empty_list(l), a)

    def test_6(self):
        self.assertEqual(get_index_from_number(7),(1,2))

    def test_7(self):
        self.assertEqual(get_index_from_number(16),(3,3))

    def test_8(self):
        self.assertEqual(get_index_from_number(1),(0,0))

    def test_9(self):
        a = []
        l = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_there_an_empty_cell(l), False)

    def test_10(self):
        a = []
        l = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_there_an_empty_cell(l), True)

    def test_11(self):
        a = []
        l = [
            [1, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 1, 1, 1],
            [0, 1, 1, 1],
        ]
        self.assertEqual(is_there_an_empty_cell(l), True)
    def test_12(self):
        a = []
        l = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        rez = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],

        ]
        self.assertEqual(move_left(l), rez)
    def test_13(self):
        a = []
        l = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4],
        ]
        rez = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0],

        ]
        self.assertEqual(move_left(l), rez)
    def test_14(self):
        a = []
        l = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        rez = [
            [4, 8, 4, 2],
            [8, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],

        ]
        self.assertEqual(move_up(l), rez)

    def test_15(self):
        a = []
        l = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 2],
            [8, 8, 4, 4],

        ]
        self.assertEqual(move_down(l), rez)

    def test_16(self):
        a = []
        l = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        self.assertEqual(is_there_a_way_out(l), True)

    def test_17(self):
        a = []
        l = [
            [2, 4, 8, 2],
            [11, 16, 5, 2],
            [9, 31, 2, 4],
            [4, 74, 34, 56],
        ]
        self.assertEqual(is_there_a_way_out(l), False)
   
    def test_18(self):
        a = []
        l = [
            [2048, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0],
        ]
        self.assertEqual(is_it_the_end(l), l)
