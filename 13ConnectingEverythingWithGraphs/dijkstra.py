import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

graph = {
    'X': [('Y', 3), ('Z', 7)],
    'Y': [('X', 3), ('Z', 1), ('W', 8)],
    'Z': [('X', 7), ('Y', 1), ('W', 2)],
    'W': [('Y', 8), ('Z', 2)]
}

print(dijkstra(graph, 'X'))
