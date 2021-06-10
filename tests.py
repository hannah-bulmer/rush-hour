import unittest

from board import *
from solve import *

class TestSolve(unittest.TestCase):

    def setUp(self):
        self.boards = from_file("jams_posted.txt")
        self.states = []
        for board in self.boards:
            self.states.append(State(board, zero_heuristic, 0, 0, None))

    def carsDontOverlap(self, board):
        arr = { '^': 0, 'v': 0, '<': 0, '>' : 0}
        cars = {'v': 0, 'h': 0}

        for row in board.grid:
            for c in row:
                if c in arr:
                    arr[c] += 1
        
        for car in board.cars:
            cars[car.orientation] += 1

        self.assertEqual(arr['v'], cars['v'])
        self.assertEqual(arr['^'], cars['v'])
        self.assertEqual(arr['<'], cars['h'])
        self.assertEqual(arr['>'], cars['h'])

    def test_blocking_heuristic(self):
        cars_blocked = [2,3,1,1,3,3,2,4,3,1,1,2,1,2,2,1]
        for i in range(0, len(cars_blocked)):
            blocked = blocking_heuristic(self.boards[i])
            self.assertEqual(blocked,cars_blocked[i]+1)


    def test_advanced_heuristic(self):
        cars_blocked = [2,4,1,2,6,4,3]
        for i in range(0, len(cars_blocked)):
            blocked = advanced_heuristic(self.boards[i])
            if blocked != cars_blocked[i]+ 1:
                self.boards[i].display()
            self.assertEqual(blocked,cars_blocked[i]+1)


    def test_advance_doms_blocking(self):
        for board in self.boards:
            self.assertGreaterEqual(advanced_heuristic(board), blocking_heuristic(board))


    def test_get_successors_no_overlap(self):
        for state in self.states:
            for new_state in get_successors(state):
                self.carsDontOverlap(new_state.board)


    def test_no_extra_successor_cars(self):
        for state in self.states:
            count = len(state.board.cars)
            for new_state in get_successors(state):
                self.assertEqual(count, len(new_state.board.cars))


    def test_count_successors(self):
        counts = [11,9,8,5,8,10,10,5,2,5,5,4,8,6,6,10,8]
        for i in range(len(counts)):
            self.assertEqual(counts[i],len(get_successors(self.states[i])))

    
    # def test_blocking_trumps_zero(self):
    #     for (indx, board) in enumerate(self.boards):
    #         print(indx)
    #         _,_, zero = a_star(board, zero_heuristic)
    #         _,_, blocking = a_star(board, blocking_heuristic)
    #         self.assertGreaterEqual(zero,blocking)

    def test_nodes_expanded(self):
        for (indx, board) in enumerate(self.boards):
            print(indx)
            _,d1, block = a_star(board, blocking_heuristic)
            _,d2, advanced = a_star(board, advanced_heuristic)
            with self.subTest(msg=f'Checking {indx} nodecount'):
                self.assertGreaterEqual(block,advanced)
            # with self.subTest(msg=f'Checking {indx} depth'):
            #     self.assertEquals(d1,d2)

    
    # def test_run_dfs(self):
    #     for board in self.boards:
    #         dfs(board)
    
if __name__ == '__main__':
    unittest.main()