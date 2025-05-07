import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, node) pairs
    pq = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}  # Set all distances to infinity
    distances[start] = 0
    previous_nodes = {node: None for node in graph}  # To reconstruct the path

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If we found the shortest path to the node, no need to process further
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Only consider this path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

# Expanded graph (adjacency list) with more nodes and edges
graph = {
    'A': [('B', 4), ('C', 1), ('D', 3)],
    'B': [('A', 4), ('C', 2), ('D', 5), ('E', 6)],
    'C': [('A', 1), ('B', 2), ('D', 4), ('E', 2)],
    'D': [('A', 3), ('B', 5), ('C', 4), ('E', 1)],
    'E': [('B', 6), ('C', 2), ('D', 1)],
}

# Run Dijkstra's algorithm starting from 'A'
distances, previous_nodes = dijkstra(graph, 'A')

# Output shortest distances from A
print("Shortest distances from A:")
for node, dist in distances.items():
    print(f"{node}: {dist}")

# To print the shortest path from A to each node
def reconstruct_path(previous_nodes, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    return path[::-1]  # Return reversed path

# Example: Shortest path from A to E
path = reconstruct_path(previous_nodes, 'A', 'E')
print(f"\nShortest path from A to E: {path}")
