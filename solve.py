from board import *
import numpy as np # for debugging

def a_star(init_board, hfn):
    """
    Run the A_star search algorithm given an initial board and a heuristic function.

    If the function finds a goal state, it returns a list of states representing
    the path from the initial state to the goal state in order and the cost of
    the solution found.
    Otherwise, it returns am empty list and -1.

    :param init_board: The initial starting board.
    :type init_board: Board
    :param hfn: The heuristic function.
    :type hfn: Heuristic
    :return: (the path to goal state, solution cost)
    :rtype: List[State], int
    """

    raise NotImplementedError


def dfs(init_board):
    """
    Run the DFS algorithm given an initial board.

    If the function finds a goal state, it returns a list of states representing
    the path from the initial state to the goal state in order and the cost of
    the solution found.
    Otherwise, it returns am empty list and -1.

    :param init_board: The initial board.
    :type init_board: Board
    :return: (the path to goal state, solution cost)
    :rtype: List[State], int
    """

    # ALSO HANDLE PRUNING 

    # frontier = [init_board state]
    # while (frontier not empty)
        # select newest elem and remove path <n0...nk> from f
        # if goal(nk): return <n0...nk>
        # for every successor n of nk:
            # add <n0...nk, n> to f

    raise NotImplementedError


def get_successors(state):
    """
    Return a list containing the successor states of the given state.
    The states in the list may be in any arbitrary order.

    :param state: The current state.
    :type state: State
    :return: The list of successor states.
    :rtype: List[State]
    """

    # given a state, we want to try moving every car every way we can
    # each way we can move a car will be a successor

    # build a 2d array keeping track of what spots are "open" for a car to move into
    # for each car, see if it can move into an "open spot" on its h/v axis

    grid = state.board.grid
    cars = state.board.cars
    successors = []

    for idx, car in enumerate(cars):
        new_cars = state.board.cars.copy()
        new_cars.pop(idx)
        temp_grid = []
        for row in grid:
            temp_grid.append(row.copy())
        if car.orientation == 'h':
            successors += slide_horizontal(car, new_cars, temp_grid, state)
        if car.orientation == 'v':
            successors += slide_vertical(car, new_cars, temp_grid, state)

    return successors


def slide_vertical(car, other_cars, grid, state):
    successors = []
    limit_top = 0
    limit_bottom = state.board.size

    if (car.orientation == 'h'): return []

    # calc top of where a car can slide to
    for indx, row in enumerate(grid):
        if row[car.fix_coord] != '.' and indx < car.var_coord:
            limit_top = indx

    # calc bottom of where a car can slide to
    for indx, row in enumerate(grid):
        if row[car.fix_coord] != '.' and indx > car.var_coord + car.length - 1:
            limit_bottom = indx

    # print(f"Top lim: {limit_top}, bottom lim: {limit_bottom}")

    row_i = limit_top
    row_j = row_i + car.length - 1
    
    # remove car from grid
    grid[car.var_coord][car.fix_coord] = '.'
    for i in range(car.length - 2):
        grid[car.var_coord+i+1][car.fix_coord] = '.'
    grid[car.var_coord+ car.length - 1][car.fix_coord] = '.'

    first_car = True

    while row_j < limit_bottom:
        invalid_state = False
        if row_i == car.var_coord or grid[row_i][car.fix_coord] != '.' or grid[row_j][car.fix_coord] != '.':
            # print(f"{row_i}, {row_j} is invalid")
            row_i += 1
            row_j += 1
            continue
        for i in range(car.length - 2):
            if grid[row_i + i + 1][car.fix_coord] != '.':
                # print(f"{row_i}, {row_j} is invalid")
                row_i += 1
                row_j += 1
                invalid_state = True
                continue

        if invalid_state: continue

        # create new board with new car
        # print(f"Moving car in col {car.fix_coord} from {car.var_coord},{car.var_coord + car.length - 1} to {row_i}, {row_j}")
        
        board = Board(state.board.name,state.board.size,other_cars + [Car(car.fix_coord,row_i,car.orientation, car.length, car.is_goal)])

        new_state = State(board, state.hfn, state.f, state.depth + 1, state)

        # new_state.board.display()

        successors.append(new_state)
        row_i += 1
        row_j += 1
    return successors

def slide_horizontal(car, other_cars, grid, state):
    successors = []
    limit_left = 0
    limit_right = state.board.size

    if (car.orientation == 'v'): return []

    # calc left of where a car can slide to
    for indx, col in enumerate(grid[car.fix_coord]):
        if col != '.' and indx < car.var_coord:
            limit_left = indx

    # calc right of where a car can slide to
    for indx, col in enumerate(grid[car.fix_coord]):
        if col != '.' and indx > car.var_coord + car.length - 1:
            limit_right = indx

    # print(f"Left lim: {limit_left}, right lim: {limit_right}")

    row_i = limit_left
    row_j = row_i + car.length - 1
    
    # remove car from grid
    grid[car.fix_coord][car.var_coord] = '.'
    for i in range(car.length - 2):
        grid[car.fix_coord][car.var_coord+i+1] = '.'
    grid[car.fix_coord][car.var_coord+ car.length - 1] = '.'

    first_car = True

    while row_j < limit_right:
        invalid_state = False
        if row_i == car.var_coord or grid[car.fix_coord][row_i] != '.' or grid[car.fix_coord][row_j] != '.':
            # print(f"{row_i}, {row_j} is invalid")
            row_i += 1
            row_j += 1
            continue
        for i in range(car.length - 2):
            if grid[car.fix_coord][row_i + i + 1] != '.':
                # print(f"{row_i}, {row_j} is invalid")
                row_i += 1
                row_j += 1
                invalid_state = True
                continue

        if invalid_state: continue

        # create new board with new car
        # print(f"Moving car in col {car.fix_coord} from {car.var_coord},{car.var_coord + car.length - 1} to {row_i}, {row_j}")
        
        board = Board(state.board.name,state.board.size,other_cars + [Car(row_i,car.fix_coord,car.orientation, car.length, car.is_goal)])

        new_state = State(board, state.hfn, state.f, state.depth + 1, state)

        # new_state.board.display()

        successors.append(new_state)
        row_i += 1
        row_j += 1
    return successors


def is_goal(state):
    """
    Returns True if the state is the goal state and False otherwise.

    :param state: the current state.
    :type state: State
    :return: True or False
    :rtype: bool
    """

    cars = state.board.cars
    for car in cars:
        if car.is_goal:
            if car.var_coord == 4:
                state.board.display()
                print("I am a goal state!")
                return True

    return False


def get_path(state):
    """
    Return a list of states containing the nodes on the path 
    from the initial state to the given state in order.

    :param state: The current state.
    :type state: State
    :return: The path.
    :rtype: List[State]
    """

    raise NotImplementedError


def blocking_heuristic(board):
    """
    Returns the heuristic value for the given board
    based on the Blocking Heuristic function.

    Blocking heuristic returns zero at any goal board,
    and returns one plus the number of cars directly
    blocking the goal car in all other states.

    :param board: The current board.
    :type board: Board
    :return: The heuristic value.
    :rtype: int
    """

    raise NotImplementedError


def advanced_heuristic(board):
    """
    An advanced heuristic of your own choosing and invention.

    :param board: The current board.
    :type board: Board
    :return: The heuristic value.
    :rtype: int
    """

    raise NotImplementedError
