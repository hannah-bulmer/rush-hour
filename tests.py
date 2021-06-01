import unittest

from board import *
from solve import *

class TestSolve(unittest.TestCase):

    def setUp(self):
        self.boards = from_file("jams_posted.txt")
        self.states = []
        for board in self.boards:
            self.states.append(State(board, zero_heuristic, 0, 0, None))

    def test_slide_vertical(self):
        state = self.states[0]
        state.board.display()
        cars = state.board.cars.copy()
        results = []
        for car in state.board.cars:
            results.append(slide_vertical(car, cars, state.board.grid, state))

        for result in results:
            print(result)

if __name__ == '__main__':
    unittest.main()