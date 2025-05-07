class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n  # For union by rank

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_mst(graph, n):
    edges = []
    for u in range(n):
        for v, w in graph[u]:
            edges.append((w, u, v))  # (weight, u, v)

    # Sort edges in increasing order of weight
    edges.sort()

    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    # Process edges in sorted order
    for weight, u, v in edges:
        if uf.union(u, v):  # If no cycle, include this edge in the MST
            mst_weight += weight
            mst_edges.append((u, v, weight))

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

# Run Kruskal's algorithm
total_weight, mst = kruskal_mst(graph, 10)

# Output
print("Minimum Spanning Tree (edges with weight):")
for u, v, w in mst:
    print(f"Node {u} - Node {v}, Weight: {w}")

print(f"\nTotal weight of MST: {total_weight}")
