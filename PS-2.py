from collections import deque

class Graph:
    def __init__(self, vertices):
        self.graph = {i: [] for i in range(vertices)}  # adjacency list
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected graph

    def bfs_recursive(self, queue, visited):
        if not queue:
            return

        current = queue.popleft()
        print(current, end=' ')

        for neighbor in self.graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        self.bfs_recursive(queue, visited)

def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    g = Graph(vertices)

    print("Enter each edge as two space-separated vertex numbers (e.g., 0 1):")
    for _ in range(edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start_vertex = int(input("Enter the starting vertex for BFS: "))
    print("\nBFS traversal:")

    visited = set([start_vertex])
    queue = deque([start_vertex])
    g.bfs_recursive(queue, visited)

if __name__ == "__main__":
    main()
