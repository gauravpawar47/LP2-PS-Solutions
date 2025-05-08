---
THOERY
---

### **A\* Algorithm (Theory)**

A\* (pronounced **A-star**) is a popular **search and pathfinding algorithm** used for finding the most efficient path from a starting point to a goal point. It combines the **best-first search** and **Dijkstra’s algorithm**, offering a balance between **optimality** and **efficiency**.

Here are the 4 main points to understand about A\*:

---

### 1. **Heuristic Search**

* A\* uses a **heuristic function** to estimate the cost of reaching the goal from a given state (node).
* This heuristic guides the search toward the goal by providing an **estimate** of the distance to the goal.
* The key idea is that A\* balances between **greedy** search (focused on getting to the goal fast) and **Dijkstra’s** search (which ensures the shortest path).

---

### 2. **Cost Function: f(n) = g(n) + h(n)**

* **g(n):** The cost to reach the current node `n` from the start node (also known as the **actual cost**).
* **h(n):** The estimated cost from node `n` to the goal (called the **heuristic**).
* **f(n) = g(n) + h(n):** Total cost function used to decide which node to explore next. Nodes with the lowest `f(n)` value are explored first.

A\* aims to minimize this cost function, ensuring that the **most promising** paths are explored first.

---

### 3. **Optimality**

* A\* is **optimal** when the heuristic function `h(n)` is **admissible**, meaning it never overestimates the actual cost to reach the goal.
* If the heuristic is **consistent** (or monotonic), A\* will also be **efficient** because it won’t revisit nodes unnecessarily.

---

### 4. **Search Process**

* **Open List:** A list of nodes that have been discovered but not yet evaluated.
* **Closed List:** A list of nodes that have already been evaluated.
* A\* starts from the **initial node** and explores nodes in the **open list** in order of increasing `f(n)`.
* Once the goal node is reached, the algorithm **stops** and returns the optimal path.
* If no solution is found, A\* will return `null`.

---

### **Summary:**

A\* is an informed search algorithm that effectively combines **greedy** and **Dijkstra's algorithm** to find the shortest path, making it optimal and efficient, especially when a good heuristic is used.

---
CODE 
---

## 🧠 Goal of the Program

Solve the **8-Queens Problem** using **A\*** Search Algorithm, where:

* You must place 8 queens on an 8x8 chessboard.
* No two queens can attack each other.
* A\* uses a cost function `f(n) = g(n) + h(n)`.

---

## 🔹 1. `State` Class – Representing Each Board Configuration

```python
class State:
    def __init__(self, queens, g):
        self.queens = queens  # List: index = row, value = column
        self.g = g  # Number of queens placed so far
        self.h = self.heuristic()  # Estimated cost to goal
        self.f = self.g + self.h  # Total cost
```

### ▶ `queens`:

* A list that represents current board state.
* Example: `[0, 4, 7]` means:

  * Row 0 → Column 0
  * Row 1 → Column 4
  * Row 2 → Column 7

### ▶ `g`:

* The actual cost: how many queens placed so far (i.e., depth in search tree).

### ▶ `h()`:

* Heuristic: Number of attacking queen pairs (to be minimized).

### ▶ `f = g + h`:

* A\*’s main cost function. Lower is better.

---

## 🔹 2. Heuristic Function

```python
def heuristic(self):
    attacks = 0
    for i in range(len(self.queens)):
        for j in range(i + 1, len(self.queens)):
            if self.queens[i] == self.queens[j] or \
               abs(self.queens[i] - self.queens[j]) == abs(i - j):
                attacks += 1
    return attacks
```

### 🔍 What it does:

* Counts the number of attacking queen pairs:

  * Same column: `queens[i] == queens[j]`
  * Same diagonal: `abs(col_diff) == abs(row_diff)`

### ✅ Why it's useful:

* You want `h = 0`, meaning no queens are attacking each other.

---

## 🔹 3. `is_goal()` Function

```python
def is_goal(self):
    return self.g == 8 and self.h == 0
```

### 🎯 Checks if:

* All 8 queens are placed (`g == 8`)
* No attacks remain (`h == 0`)

---

## 🔹 4. `__lt__()` – Comparison for Priority Queue

```python
def __lt__(self, other):
    return self.f < other.f
```

### 🔑 Why it exists:

* Required for `heapq`, so it knows how to sort `State` objects.
* Compares based on `f` value (lower = higher priority).

---

## 🔹 5. Generating Next States

```python
def get_successors(state):
    successors = []
    row = len(state.queens)  # Next row to place queen
    if row >= 8:
        return successors

    for col in range(8):
        new_queens = state.queens + [col]
        new_state = State(new_queens, state.g + 1)
        successors.append(new_state)

    return successors
```

### 🧱 What it does:

* Tries placing a queen in **next row** at **each column (0 to 7)**.
* Creates a new state for each.

---

## 🔹 6. A\* Search Algorithm

```python
def a_star_8_queens():
    initial_state = State([], 0)  # No queens placed
    open_list = []
    heapq.heappush(open_list, initial_state)

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            return current.queens

        for successor in get_successors(current):
            if successor.h == 0 or successor.g < 8:
                heapq.heappush(open_list, successor)

    return None
```

### 🧠 How it works:

* Starts with an empty board.
* Picks the state with **lowest f = g + h**.
* Expands it (places next queen in each column).
* Continues until goal is found (8 safe queens).

### 🔍 The `if successor.h == 0 or successor.g < 8` line:

* Helps **prune bad branches** where attacks are already present.
* Only explores promising states.

---

## 🔹 7. Display the Solution

```python
solution = a_star_8_queens()

if solution:
    print("Solution (row index is row, value is column):")
    print(solution)

    print("\nBoard:")
    for row in range(8):
        line = ['Q' if solution[row] == col else '.' for col in range(8)]
        print(' '.join(line))
else:
    print("No solution found.")
```

### 📋 Output:

* Shows `solution` as a list (row -> col).
* Prints a nice board with `'Q'` and `'.'`.

---

## ✅ Summary of A\* in this code

* **Initial State:** Empty board.
* **Successor Function:** Place a queen in the next row, in each column.
* **g(n):** Number of queens placed.
* **h(n):** Number of queen attack conflicts.
* **f(n):** Total cost = g + h.
* **Goal State:** All 8 queens placed with no conflicts.

---
ALGORITHM
---

```
ALGORITHM A_STAR_8_QUEENS
---------------------------
1. Define a class State:
   a. queens: List of queen positions (index = row, value = column)
   b. g = number of queens placed (depth)
   c. h = number of attacking pairs among placed queens
   d. f = g + h

2. Define heuristic(state):
   a. Initialize attacks = 0
   b. For each pair of queens (i, j):
      - If same column OR on same diagonal:
          attacks += 1
   c. Return attacks

3. Define is_goal(state):
   Return True if g == 8 AND h == 0

4. Define get_successors(state):
   a. row = number of queens placed = len(state.queens)
   b. For col from 0 to 7:
      - new_queens = state.queens + [col]
      - Create new_state with new_queens and g+1
      - Add new_state to successors

5. Define A_STAR_8_QUEENS():
   a. Create initial_state with empty queen list, g = 0
   b. Add initial_state to priority queue (min-heap based on f)

   c. While priority queue is not empty:
      i. Pop current state from heap
     ii. If current is goal: return current.queens
    iii. For each successor of current:
            - If g < 8 or h == 0 (to prune invalid branches):
                Add successor to heap

   d. If no solution found, return None

6. Print board from final queens list

END
```