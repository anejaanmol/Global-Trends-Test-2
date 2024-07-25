# Write a function to find the shortest path from a source vertex to all other vertices in a graph using Dijkstra's algorithm.
import heapq

def dijkstra(graph, source):
    pq = [(0, source)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# giVEN TEST CASE 
graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}
source = 0
print(dijkstra(graph, source))  
