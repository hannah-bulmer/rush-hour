import unittest

from board import *
from solve import *

class TestSolve(unittest.TestCase):

    def setUp(self):
        self.boards = from_file("jams_posted.txt")
        self.states = []
        for board in self.boards:
            self.states.append(State(board, zero_heuristic, 0, 0, None))


    def test_blocking_heuristic(self):
        cars_blocked = [2,3,1,1,3,3,2,4,3,1,1,2,1,2,2,1]
        for i in range(0, len(cars_blocked)):
            blocked = blocking_heuristic(self.boards[i])
            self.assertEquals(blocked,cars_blocked[i]+1)


    def test_advanced_heuristic(self):
        cars_blocked = [5,4,1,3,6,5,2,6,3,2,3,5,2,2,4,3]
        for i in range(0, len(cars_blocked)):
            blocked = advanced_heuristic(self.boards[i])
            self.assertEquals(blocked,cars_blocked[i]+1)


    def test_advance_doms_blocking(self):
        for board in self.boards:
            self.assertGreaterEqual(advanced_heuristic(board), blocking_heuristic(board))

if __name__ == '__main__':
    unittest.main()