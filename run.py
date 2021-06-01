from board import *
from solve import *

def main():
    boards = from_file("jams_posted.txt")

    states = []
    for board in boards:
        states.append(State(board, zero_heuristic, 0, 0, None))

    states[0].board.display()
    successors = get_successors(states[0])

    for s in successors:
        s.board.display()

if __name__ == "__main__":
    main()