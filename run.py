from board import *
from solve import *

def main():
    boards = from_file("jams_posted.txt")

    states = []
    for board in boards:
        # board.display()
        # blocking_heuristic(board)
        # advanced_heuristic(board)
        states.append(State(board, zero_heuristic, 0, 0, None))

    num = 10
    dfs(states[num].board)
    a_star(states[num].board, zero_heuristic)
    a_star(states[num].board, blocking_heuristic)
    a_star(states[num].board, advanced_heuristic)

if __name__ == "__main__":
    main()