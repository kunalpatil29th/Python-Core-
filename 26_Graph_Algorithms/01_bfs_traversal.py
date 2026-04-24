"""
PROPER DEFINITION:
Breadth-First Search (BFS) is a graph traversal algorithm that starts at a selected node (the 'source') 
and explores all its neighbor nodes at the present depth before moving on to the nodes at the next 
depth level. It uses a Queue (First-In-First-Out) data structure to keep track of the nodes to be 
visited. BFS is particularly useful for finding the shortest path in an unweighted graph.
"""

from collections import deque

def bfs(graph, start_node):
    print(f"--- Breadth-First Search (BFS) starting from node: {start_node} ---")
    
    # Keep track of visited nodes to avoid infinite loops in cyclic graphs
    visited = set()
    # Initialize the queue with the starting node
    queue = deque([start_node])
    # Mark the start node as visited
    visited.add(start_node)
    
    traversal_path = []

    while queue:
        # Dequeue a vertex from the queue
        current_node = queue.popleft()
        traversal_path.append(current_node)
        
        # Get all adjacent vertices of the dequeued vertex
        # If an adjacent has not been visited, mark it visited and enqueue it
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_path

if __name__ == "__main__":
    # Example Graph represented as an Adjacency List
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    path = bfs(graph, 'A')
    print(f"BFS Traversal Path: {' -> '.join(path)}")
