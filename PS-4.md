
### 📘 PS-4: N-Puzzle using A*

---

## 🧠 **Goal of the Program**

The goal of this program is to solve the **8-puzzle problem** using the **A\*** search algorithm. In the 8-puzzle problem, we are given a 3x3 grid where one tile is blank (represented as 0). The objective is to move the tiles around in order to reach a goal state, which is:

```
1 2 3
4 5 6
7 8 0
```

The challenge is to find the optimal sequence of moves (the least number of steps) to transform the initial board configuration into the goal configuration. We will use **A\*** algorithm, which is an informed search algorithm, to solve this problem.

---

## 📝 **Theory**

### **A\* Algorithm (Theory)**

A\* (pronounced **A-star**) is an efficient and popular search algorithm used to find the shortest path between nodes. It is particularly useful in pathfinding problems such as the **8-puzzle**, where the algorithm uses both **greedy search** and **Dijkstra’s algorithm** principles.

Here’s how A\* works in the context of the 8-puzzle:

### 1. **State Representation**

Each state represents a configuration of the 3x3 board. We start from an initial configuration and explore different states by moving the blank tile around.

### 2. **Cost Function: f(n) = g(n) + h(n)**

* **g(n):** The cost to reach the current state (number of moves taken so far).
* **h(n):** The heuristic estimate of the cost to reach the goal from the current state. In this case, **Manhattan distance** is used as the heuristic, which calculates the sum of the absolute differences in the row and column positions of each tile from its goal position.
* **f(n):** The total estimated cost of the path, given by `f(n) = g(n) + h(n)`.

A\* explores the states with the lowest `f(n)` first, ensuring that the most promising paths are considered first.

### 3. **Heuristic: Manhattan Distance**

For each tile, we calculate the **Manhattan distance**—the sum of the horizontal and vertical distances from the tile’s current position to its goal position. The total heuristic value is the sum of the Manhattan distances for all tiles.

### 4. **Optimality**

A\* is guaranteed to find the optimal solution if the heuristic function is **admissible** (i.e., it does not overestimate the cost to reach the goal).

---

## 🔹 **Code Explanation**

### **1. PuzzleState Class – Representing Each Board Configuration**

```python
class PuzzleState:
    def __init__(self, board, g, parent=None):
        self.board = board
        self.g = g  # Number of moves from the start
        self.h = self.heuristic()  # Estimated cost to goal
        self.f = self.g + self.h  # Total cost function
        self.parent = parent  # Parent state to reconstruct the solution path
```

* **board**: A 3x3 grid representing the current configuration of the puzzle.
* **g**: The number of moves taken to reach the current configuration.
* **h**: The Manhattan distance from the current configuration to the goal.
* **f = g + h**: The total cost function used for ordering nodes.

### **2. Heuristic Function**

```python
def heuristic(self):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = self.board[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance
```

* This function calculates the **Manhattan distance** for all tiles, except the blank tile (0). The total heuristic value is the sum of these distances.

### **3. Generate Successors (Valid Moves)**

```python
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
```

* This function generates all valid successor states by moving the blank tile in all possible directions (up, down, left, right). It checks for boundary conditions and adds each valid move to the list of successors.

### **4. Goal Check**

```python
def is_goal(self):
    return self.board == GOAL_STATE
```

* This function checks if the current board configuration matches the goal state.

### **5. Comparison for Priority Queue**

```python
def __lt__(self, other):
    return self.f < other.f
```

* This comparison is necessary for using a **min-heap** (`heapq`) to prioritize exploring states with the smallest `f(n)`.

### **6. A\* Search Algorithm**

```python
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
```

* **open\_list**: A priority queue (min-heap) that stores states ordered by `f(n)`.
* **closed\_set**: A set to keep track of explored states to avoid re-exploration.
* The algorithm continues until a solution is found or the open list is empty.

### **7. Reconstruct Path**

```python
def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.parent
    return path[::-1]
```

* This function reconstructs the path from the start to the goal by following the parent pointers of each state.

### **8. Display Board**

```python
def print_board(board):
    for row in board:
        print(' '.join(str(cell) if cell != 0 else ' ' for cell in row))
    print()
```

* This function prints the current board configuration in a readable format, with a blank tile displayed as a space.

---

## 🔹 **Algorithm**

```
ALGORITHM A_STAR_8_PUZZLE
--------------------------
1. Define PuzzleState class:
   a. board: Current configuration of the puzzle (3x3 grid)
   b. g: Number of moves from start to current state
   c. h: Heuristic (Manhattan distance to goal)
   d. f = g + h

2. Define heuristic function:
   a. For each tile, calculate its Manhattan distance to the goal.
   b. Return the sum of these distances.

3. Define generate_successors function:
   a. Get the position of the blank tile (0).
   b. For each valid move (up, down, left, right):
      - Swap the blank tile with the adjacent tile.
      - Create a new PuzzleState with the new board and increment g by 1.

4. Define is_goal function:
   Return True if the board is equal to the goal state.

5. Define A_STAR_8_PUZZLE:
   a. Create initial state with the given start_board.
   b. Add initial state to open list (min-heap).
   c. While the open list is not empty:
      i. Pop the state with the lowest f-value.
     ii. If the state is the goal, reconstruct the solution path.
    iii. For each successor of the current state:
          - If the successor has not been explored, add it to the open list.

6. If no solution is found, return None.

END
```

---