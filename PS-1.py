class Graph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}  # adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # since the graph is undirected

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Dynamic input
def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    g = Graph(vertices)

    print("Enter each edge as two space-separated vertex numbers (e.g., 0 1):")
    for _ in range(edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start_vertex = int(input("Enter the starting vertex for DFS: "))
    print("\nDFS traversal:")
    g.dfs(start_vertex)

if __name__ == "__main__":
    main()
