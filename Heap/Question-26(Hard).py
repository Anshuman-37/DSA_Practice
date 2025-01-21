# Question 26: Implement Dijkstra’s Algorithm using a min-heap.
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        dist, current_node = heapq.heappop(min_heap)

        if dist > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, {}).items():
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5, 'C': 1},
    'C': {'B': 1, 'D': 8, 'E': 10},
    'D': {'E': 2},
    'E': {'F': 3},
    'F': {}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print(f"Shortest distances from {start_node}: {shortest_distances}")