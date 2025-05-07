class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
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

    # Sort edges by weight
    edges.sort()

    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    # Process edges in increasing order of weight
    for weight, u, v in edges:
        if uf.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))

    return mst_weight, mst_edges

# Example graph (adjacency list) with more nodes and edges
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

# Run Kruskal's Greedy MST Algorithm
total_weight, mst = kruskal_mst(graph, len(graph))

# Output
print("Minimum Spanning Tree edges (u, v, edge weight):")
for u, v, w in mst:
    print(f"Node {u} - Node {v}, Edge Weight: {w}")
print(f"\nTotal weight of MST: {total_weight}")
