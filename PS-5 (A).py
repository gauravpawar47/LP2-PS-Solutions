import heapq

def prim_mst(graph, start=0):
    visited = set()
    min_heap = [(0, start)]  # (weight, vertex)
    mst_weight = 0
    mst_edges = []

    while min_heap and len(visited) < len(graph):
        weight, u = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)
        mst_weight += weight

        if weight != 0:
            mst_edges.append((u, weight))

        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))

    return mst_weight, mst_edges

# Example static undirected graph represented as adjacency list
# Format: graph[node] = [(neighbor, weight), ...]
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

# Run Prim's Greedy MST Algorithm
total_weight, mst = prim_mst(graph)

# Output
print("Minimum Spanning Tree edges (node, edge weight):")
for u, w in mst:
    print(f"Node {u}, Edge Weight: {w}")
print(f"\nTotal weight of MST: {total_weight}")
