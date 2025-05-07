import heapq

class State:
    def __init__(self, queens, g):
        self.queens = queens  # List where index = row, value = column
        self.g = g  # Cost to reach current state (queens placed so far)
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        # Count number of attacking pairs
        attacks = 0
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                if self.queens[i] == self.queens[j] or \
                   abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    attacks += 1
        return attacks

    def is_goal(self):
        return self.g == 8 and self.h == 0

    def __lt__(self, other):
        return self.f < other.f

def get_successors(state):
    successors = []
    row = len(state.queens)
    if row >= 8:
        return successors

    for col in range(8):
        new_queens = state.queens + [col]
        new_state = State(new_queens, state.g + 1)
        successors.append(new_state)
    return successors

def a_star_8_queens():
    initial_state = State([], 0)
    open_list = []
    heapq.heappush(open_list, initial_state)

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            return current.queens

        for successor in get_successors(current):
            if successor.h == 0 or successor.g < 8:  # Prune only valid branches
                heapq.heappush(open_list, successor)

    return None

# Run the algorithm
solution = a_star_8_queens()

# Display the solution
if solution:
    print("Solution (row index is row, value is column):")
    print(solution)

    print("\nBoard:")
    for row in range(8):
        line = ['Q' if solution[row] == col else '.' for col in range(8)]
        print(' '.join(line))
else:
    print("No solution found.")
