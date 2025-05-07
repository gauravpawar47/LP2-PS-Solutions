def is_safe(graph, color, v, c):
    # Check if this color can be assigned to vertex v
    for neighbor in graph[v]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0

    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)  # Initialize color array
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist")
        return False

    print(f"Solution found with {m} colors: {color}")
    return True

# Test the Graph Coloring Solution for a 4-node graph and 2 colors
print("Graph Coloring Solution for 4 nodes with 2 colors:")
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

graph_coloring(graph, 3)
