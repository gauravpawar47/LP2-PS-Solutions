---
Algorithm
---

1. Start
2. Initialize a graph with 'n' vertices using an adjacency list
3. For each edge:
     a. Take input (u, v)
     b. Add v to adjacency list of u
     c. Add u to adjacency list of v (undirected)
4. Take input: start_vertex
5. Initialize:
     a. visited set with start_vertex
     b. queue with start_vertex

6. Call BFS(queue, visited)

Procedure BFS(queue, visited):
   a. If queue is empty, return
   b. Pop front element from queue → current
   c. Print current
   d. For each neighbor of current in graph:
        i. If neighbor not in visited:
           - Add neighbor to visited
           - Enqueue neighbor
   e. Call BFS(queue, visited) again (recursion)

7. End

---


Sure! Let's break down the code step-by-step. This code defines an **undirected graph** and performs **recursive Breadth-First Search (BFS)** starting from a user-defined vertex.

---

### 🔍 **1. Graph Class Initialization**

```python
class Graph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}  # adjacency list
        self.vertices = vertices
```

* `vertices`: Number of vertices in the graph.
* `self.graph`: Dictionary representing the adjacency list (each key is a vertex, and the value is a list of its neighbors).

---

### 🔧 **2. Adding Edges**

```python
def add_edge(self, u, v):
    self.graph[u].append(v)
    self.graph[v].append(u)  # undirected graph
```

* Adds an edge between `u` and `v`.
* Since it's an undirected graph, both `u -> v` and `v -> u` are added.

---

### 🔁 **3. Recursive BFS Function**

```python
def bfs_recursive(self, queue, visited):
    if not queue:
        return

    current = queue.popleft()
    print(current, end=' ')
```

* **`queue`**: Stores vertices to be processed (FIFO, typical BFS style).
* **`visited`**: A `set` to track visited nodes.
* It removes the front node of the queue and processes it.

```python
    for neighbor in self.graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

* Iterates over neighbors of the current node.
* If a neighbor hasn’t been visited yet, it's added to `visited` and enqueued for processing.

```python
    self.bfs_recursive(queue, visited)
```

* Recursively calls itself with the updated queue and visited set.

🔁 This keeps running until the queue becomes empty.

---

### 🚀 **4. Main Function Flow**

```python
def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
```

* Takes input for number of vertices and edges.

```python
    g = Graph(vertices)
    ...
    for _ in range(edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)
```

* Creates a graph object and adds the given edges.

```python
    start_vertex = int(input("Enter the starting vertex for BFS: "))
    print("\nBFS traversal:")

    visited = set([start_vertex])
    queue = deque([start_vertex])
    g.bfs_recursive(queue, visited)
```

* Initializes BFS from the `start_vertex`.
* Starts with that vertex in both `queue` and `visited`.
* Calls the recursive BFS.

---

### 🧠 Summary

* **Recursive BFS** is less common than iterative BFS, but this code makes it work by:

  * Using a `deque` to simulate queue behavior.
  * Using a `set` to track visited nodes.
  * Processing nodes level-by-level, printing them in BFS order.

✅ BFS is typically implemented iteratively using a loop, but this recursive version is functionally equivalent.

---
