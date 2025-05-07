import heapq

def prim_mst(graph, start=0):
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)
    mst_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        mst_weight += weight

        if weight != 0:  # We don't add the starting node itself
            mst_edges.append((u, weight))

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))

    return mst_weight, mst_edges

# Example graph (adjacency list) with 10 nodes and more edges
graph = {
    0: [(1, 2), (3, 6), (4, 3)],
    1: [(0, 2), (2, 4), (4, 5), (5, 6)],
    2: [(1, 4), (3, 8), (5, 7), (6, 5)],
    3: [(0, 6), (2, 8), (6, 9)],
    4: [(0, 3), (1, 5), (5, 8), (6, 2)],
    5: [(1, 6), (2, 7), (4, 8), (6, 1)],
    6: [(2, 5), (3, 9), (4, 2), (5, 1), (7, 3)],
    7: [(6, 3), (8, 7), (9, 4)],
    8: [(7, 7), (9, 5)],
    9: [(7, 4), (8, 5)]
}

# Run Prim's Greedy MST Algorithm starting from node 0
total_weight, mst = prim_mst(graph)

# Output
print("Minimum Spanning Tree (edges with weight):")
for u, w in mst:
    print(f"Node {u}, Weight: {w}")

print(f"\nTotal weight of MST: {total_weight}")
