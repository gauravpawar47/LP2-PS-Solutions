### 📘 PS-5 (A): Minimum Spanning Tree using Prim's Algorithm

---

### **Prim’s Algorithm (Theory)**

Prim’s Algorithm is a **greedy algorithm** used to find the **minimum spanning tree (MST)** of a connected, undirected graph. The **minimum spanning tree** is a subset of the edges that connects all the vertices in the graph, with the minimum possible total edge weight, and without any cycles.

Here are the 4 main points to understand about Prim's Algorithm:

---

### 1. **Greedy Approach**

* Prim’s algorithm works by starting with a single vertex and then iteratively adding the smallest edge that connects a vertex in the MST to a vertex outside the MST.
* This approach ensures that each added edge has the minimum possible weight, thus leading to the MST.

---

### 2. **Steps of the Algorithm**

* Start from an arbitrary vertex (usually vertex 0).
* Mark the starting vertex as part of the MST.
* Add the minimum weight edge that connects a vertex in the MST to a vertex outside the MST.
* Repeat this process until all vertices are included in the MST.

---

### 3. **Priority Queue**

* A priority queue (implemented using a **min-heap**) is used to efficiently get the next minimum weight edge.
* The priority queue stores the edges that could potentially be added to the MST, ordered by edge weight.

---

### 4. **Optimality**

* Prim’s algorithm guarantees an **optimal solution** (minimum spanning tree) because it always selects the minimum weight edge at each step and adds it to the MST.
* This ensures that the total weight of the MST is minimized.

---

### **Summary:**

Prim's algorithm is an efficient, greedy algorithm for finding the minimum spanning tree of a graph. It works by growing the MST one edge at a time, always adding the edge with the minimum weight that connects a vertex in the MST to a vertex outside it.

---

### CODE

---

## 🧠 Goal of the Program

Implement Prim’s algorithm to compute the **Minimum Spanning Tree (MST)** of a given undirected graph. The graph is represented using an adjacency list, and the algorithm should find the total weight of the MST along with the edges included in it.

### 1. **Importing heapq Module**

```python
import heapq
```

* The `heapq` module is imported to use a priority queue (min-heap), which helps to efficiently retrieve the minimum weight edge during the MST computation.

---

### 2. **Defining the Prim's MST Function**

```python
def prim_mst(graph, start=0):
```

* This defines a function `prim_mst` that takes a graph (as an adjacency list) and a starting node (`start`, which defaults to 0) as parameters. The goal of this function is to find the Minimum Spanning Tree (MST) of the graph using Prim's algorithm.

---

### 3. **Initial Setup**

```python
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)
    mst_weight = 0
    mst_edges = []
```

* `visited = set()`:

  * A set `visited` is initialized to keep track of the nodes that have already been added to the MST.

* `min_heap = [(0, start)]`:

  * `min_heap` is a priority queue (min-heap) that stores tuples of the form `(weight, vertex)`. The algorithm starts with the `start` node and a weight of `0` (since no edge is considered to start the MST).

* `mst_weight = 0`:

  * The total weight of the MST is initialized to `0`.

* `mst_edges = []`:

  * A list `mst_edges` is initialized to store the edges that will be part of the MST.

---

### 4. **Main While Loop**

```python
    while min_heap and len(visited) < len(graph):
```

* This loop runs while the priority queue `min_heap` is not empty and the number of visited nodes is less than the total number of nodes in the graph. This ensures that the MST includes all the nodes.

---

### 5. **Extracting the Minimum Weight Edge**

```python
        weight, u = heapq.heappop(min_heap)
```

* `heapq.heappop(min_heap)` pops the element with the smallest weight from the priority queue.

  * `weight` is the weight of the edge being considered.
  * `u` is the vertex (node) that this edge leads to.

---

### 6. **Skip If Node Already Visited**

```python
        if u in visited:
            continue
```

* If the node `u` has already been added to the MST (i.e., it's in the `visited` set), this iteration is skipped, ensuring that the algorithm doesn't revisit nodes.

---

### 7. **Add Node to MST**

```python
        visited.add(u)
        mst_weight += weight
```

* `visited.add(u)` adds the node `u` to the `visited` set, indicating that it has been included in the MST.
* `mst_weight += weight` adds the weight of the edge (`weight`) to the total MST weight.

---

### 8. **Add Edge to MST (if weight != 0)**

```python
        if weight != 0:
            mst_edges.append((u, weight))
```

* If the weight of the edge is not 0 (i.e., it's not the initial "starting" edge), the edge `(u, weight)` is added to `mst_edges`, indicating that the edge is part of the MST.

---

### 9. **Adding Neighbors to the Priority Queue**

```python
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))
```

* This loop iterates over the neighbors of the current node `u` (i.e., for each `(v, w)` pair where `v` is a neighboring node and `w` is the weight of the edge between `u` and `v`).
* If the neighbor `v` has not yet been visited, it is added to the priority queue `min_heap` with the edge's weight `w`.

---

### 10. **Return the Result**

```python
    return mst_weight, mst_edges
```

* Once the while loop ends, the function returns two values:

  * `mst_weight`: The total weight of the MST.
  * `mst_edges`: The list of edges that form the MST.

---

### Example Graph Definition

```python
graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    2: [(1, 8), (3, 7), (5, 4), (8, 2)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(2, 4), (3, 14), (4, 10), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(2, 2), (6, 6), (7, 7)]
}
```

* This is a static graph represented as an adjacency list, where:

  * Each node (key) has a list of tuples representing its neighbors and the weight of the edges connecting them.

---

### Running the Prim's Algorithm and Displaying the Result

```python
total_weight, mst = prim_mst(graph)
```

* The `prim_mst()` function is called with the `graph`, and it returns the total weight of the MST (`total_weight`) and the list of edges in the MST (`mst`).

---

### Output the Results

```python
print("Minimum Spanning Tree edges (node, edge weight):")
for u, w in mst:
    print(f"Node {u}, Edge Weight: {w}")
print(f"\nTotal weight of MST: {total_weight}")
```

* The edges of the Minimum Spanning Tree (`mst`) are printed, with each edge showing the node and the corresponding edge weight.
* The total weight of the MST is also printed.

---

### Example Output

```plaintext
Minimum Spanning Tree edges (node, edge weight):
Node 0, Edge Weight: 4
Node 1, Edge Weight: 8
Node 2, Edge Weight: 7
Node 5, Edge Weight: 4
Node 6, Edge Weight: 2
Node 7, Edge Weight: 1
Node 8, Edge Weight: 2

Total weight of MST: 28
```

### ALGORITHM

```
ALGORITHM PRIM_MST
-------------------
1. Define a function `prim_mst(graph, start=0)`:
   a. Create a set `visited` to track visited vertices.
   b. Create a min-heap `min_heap` to store edges with their weights.
   c. Initialize variables `mst_weight` (total weight of MST) and `mst_edges` (list of MST edges).
   
2. While `min_heap` is not empty and `visited` doesn't contain all vertices:
   a. Pop the minimum weight edge `(weight, u)` from `min_heap`.
   b. If `u` is already in `visited`, continue to the next iteration.
   c. Add `u` to `visited`.
   d. Add the weight to `mst_weight` and append the edge `(u, weight)` to `mst_edges`.
   
3. For each neighbor `(v, w)` of `u`, if `v` is not in `visited`:
   a. Push the edge `(w, v)` into `min_heap`.

4. Return the total MST weight and list of edges in the MST.

5. Print the MST edges and total weight.

END
```
