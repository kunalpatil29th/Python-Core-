"""
PROPER DEFINITION:
Dijkstra's Algorithm is a graph search algorithm that finds the shortest path between a 
starting node and all other nodes in a weighted graph with non-negative edge weights. 
It works by maintaining a set of 'tentative distances' and greedily selecting the node 
with the smallest tentative distance to explore next. It typically uses a Priority Queue 
(Min-Heap) to efficiently find the next node to visit.
"""

import heapq

def dijkstra(graph, start):
    print(f"--- Dijkstra's Algorithm starting from: {start} ---")
    
    # Initialize distances to all nodes as infinity, and start node as 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue stores (distance, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we found a longer path than already recorded, skip it
        if current_distance > distances[current_node]:
            continue
            
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If a shorter path is found, update and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

if __name__ == "__main__":
    # Example Weighted Graph
    # Format: {node: {neighbor: weight}}
    weighted_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 5, 'D': 10},
        'C': {'E': 3},
        'D': {'F': 11},
        'E': {'D': 4},
        'F': {}
    }
    
    shortest_distances = dijkstra(weighted_graph, 'A')
    
    print("\nShortest distances from node 'A':")
    for node, distance in shortest_distances.items():
        print(f"To {node}: {distance}")
