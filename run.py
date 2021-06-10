import os
from board import *
from solve import *

os.environ["PYTHONHASHSEED"] = "486"

def main():
    boards = from_file("jams_posted.txt")

    # boards[3].display()
    # boards[4].display()
    # boards[5].display()
    # boards[6].display()

    states = []
    for board in boards:
        # board.display()
        # blocking_heuristic(board)
        # advanced_heuristic(board)
        states.append(State(board, advanced_heuristic, 0, 0, None))

    num = 27
    boards[num].display()
    successors = get_successors(states[num])
    print(f"Num successors: {len(successors)}")
    for s in successors:
        s.board.display()


    # num = 6
    # for num in range(40):
    # dfs(states[num].board)
    # a_star(states[num].board, zero_heuristic)
    # a_star(states[num].board, blocking_heuristic)
    # a_star(states[num].board, advanced_heuristic)

    # for i in range(41,len(boards)):
    #     boards[i].display()

    # print(len(get_successors(states[41])))

    # successors = get_successors(states[2])

    # for s in successors:
    #     print(len(get_successors(s)))

    # states[15].board.display()
    # for s in successors:
    #     s.board.display()

if __name__ == "__main__":
    main()