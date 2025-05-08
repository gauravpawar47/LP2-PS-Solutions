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
5. Initialize an empty set 'visited'

6. Call DFS(start_vertex, visited)

Procedure DFS(node, visited):
   a. Add node to visited
   b. Print node
   c. For each neighbor of node in graph:
       i. If neighbor is not in visited:
          - Call DFS(neighbor, visited)

7. End

---



This is a clean and standard implementation of **Depth-First Search (DFS)** using **recursion** on an **undirected graph**. Here's a detailed explanation of how this code works:

---

### 🔧 **1. Graph Class**

```python
class Graph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}  # adjacency list
```

* Creates an **adjacency list** for a graph with `vertices` number of nodes.
* Initially, each node has an empty list of neighbors.

---

### ➕ **2. Edge Addition**

```python
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected
```

* Adds an undirected edge: both `u -> v` and `v -> u`.

---

### 🔁 **3. DFS Function**

```python
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
```

* Initializes a `visited` set on the first call (to avoid using a global variable).

```python
        visited.add(start)
        print(start, end=' ')
```

* Marks the `start` node as visited and prints it.

```python
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)
```

* Recursively visits all unvisited neighbors of the current node — this is the core of DFS.

---

### 🏁 **4. Main Function**

```python
def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
```

* Takes input for number of vertices and edges.

```python
    g = Graph(vertices)

    print("Enter each edge as two space-separated vertex numbers (e.g., 0 1):")
    for _ in range(edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)
```

* Builds the graph dynamically based on user input.

```python
    start_vertex = int(input("Enter the starting vertex for DFS: "))
    print("\nDFS traversal:")
    g.dfs(start_vertex)
```

* Reads the starting point for DFS, then calls `dfs()` to perform the traversal and print nodes in the correct DFS order.

---

### ✅ Example Input and Output

If you input:

```
Enter the number of vertices: 10  
Enter the number of edges: 9  
Enter each edge as two space-separated vertex numbers (e.g., 0 1):  
0 1  
0 2  
1 3  
1 4  
3 7  
3 8  
2 5  
2 6  
6 9  
Enter the starting vertex for DFS: 0
```

Then output will be:

```
DFS traversal:  
0 1 3 7 8 4 2 5 6 9
```

Which is correct based on the depth-first logic.

---

Would you like the same implementation using an **explicit stack (iterative DFS)** instead of recursion?

