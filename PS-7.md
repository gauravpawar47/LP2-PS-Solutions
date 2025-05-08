| Criteria                | **Prim’s Algorithm**                              | **Kruskal’s Algorithm**                       |
| ----------------------- | ------------------------------------------------- | --------------------------------------------- |
| **Graph Type**          | Better for **dense graphs**                       | Better for **sparse graphs**                  |
| **Data Structure Used** | Min-heap (priority queue) + Adjacency list/matrix | Disjoint Set (Union-Find) + Edge List         |
| **Edge Sorting?**       | Not required                                      | Required (sort all edges first)               |
| **Time Complexity**     | O(E + log V) with Fibonacci heap                  | O(E log E) or O(E log V) with Union-Find      |
| **Key Operation**       | Extract min edge from current MST                 | Pick smallest edge that connects 2 components |
