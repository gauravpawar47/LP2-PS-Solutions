import heapq

# Goal state for 8-puzzle
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the blank tile

# Moves: (dx, dy)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

class PuzzleState:
    def __init__(self, board, g, parent=None):
        self.board = board
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h
        self.parent = parent

    def heuristic(self):
        # Manhattan distance
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    goal_x = (value - 1) // 3
                    goal_y = (value - 1) % 3
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        x, y = self.get_blank_position()
        for dx, dy in MOVES:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                successors.append(PuzzleState(new_board, self.g + 1, self))
        return successors

    def is_goal(self):
        return self.board == GOAL_STATE

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(str(self.board))

    def __eq__(self, other):
        return self.board == other.board

def a_star(start_board):
    start_state = PuzzleState(start_board, 0)
    open_list = []
    heapq.heappush(open_list, start_state)
    closed_set = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            return reconstruct_path(current)

        closed_set.add(hash(current))

        for neighbor in current.generate_successors():
            if hash(neighbor) in closed_set:
                continue
            heapq.heappush(open_list, neighbor)

    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]

def print_board(board):
    for row in board:
        print(' '.join(str(cell) if cell != 0 else ' ' for cell in row))
    print()

# Example initial configuration
initial_board = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

# Print initial state
print("Initial State:")
print_board(initial_board)

# Run A* algorithm
solution_path = a_star(initial_board)

# Display the solution
if solution_path:
    print(f"Solution found in {len(solution_path) - 1} moves:\n")
    for step, board in enumerate(solution_path):
        print(f"Step {step}:")
        print_board(board)
else:
    print("No solution found.")
