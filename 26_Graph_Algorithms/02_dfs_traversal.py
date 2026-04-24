"""
PROPER DEFINITION:
Depth-First Search (DFS) is a graph traversal algorithm that starts at a selected node and explores 
as far as possible along each branch before backtracking. It can be implemented using recursion 
(which uses the call stack) or an explicit Stack (Last-In-First-Out). DFS is commonly used for 
topological sorting, finding connected components, and solving puzzles like mazes.
"""

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(node)
    print(f"Visited: {node}")
    
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited

def dfs_iterative(graph, start_node):
    print(f"\n--- Depth-First Search (DFS) Iterative starting from: {start_node} ---")
    visited = set()
    stack = [start_node]
    traversal_path = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_path.append(node)
            # Add neighbors to stack (reversed to match recursive order if needed)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_path

if __name__ == "__main__":
    # Example Graph represented as an Adjacency List
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    print("--- DFS Recursive ---")
    dfs_recursive(graph, 'A')
    
    path = dfs_iterative(graph, 'A')
    print(f"DFS Iterative Traversal Path: {' -> '.join(path)}")
