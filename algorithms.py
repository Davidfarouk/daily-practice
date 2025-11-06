def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return -1

# Graph Data Structures
class Graph:
    """Graph implementation using adjacency list"""
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        """Add edge from u to v"""
        self.adj_list[u].append(v)

    def get_adjacency_list(self):
        return self.adj_list

class GraphMatrix:
    """Graph implementation using adjacency matrix"""
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        """Add edge from u to v with optional weight"""
        self.adj_matrix[u][v] = weight

    def get_adjacency_matrix(self):
        return self.adj_matrix

# Graph Algorithms
def bfs(graph, start):
    """
    Breadth-First Search algorithm
    Args:
        graph: Graph object with adjacency list
        start: starting vertex
    Returns:
        list of vertices in BFS order
    """
    from collections import deque

    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.adj_list.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

def dfs(graph, start, visited=None):
    """
    Depth-First Search algorithm (recursive)
    Args:
        graph: Graph object with adjacency list
        start: starting vertex
        visited: set of visited vertices
    Returns:
        list of vertices in DFS order
    """
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.adj_list.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))

    return result

def dfs_iterative(graph, start):
    """
    Depth-First Search algorithm (iterative)
    Args:
        graph: Graph object with adjacency list
        start: starting vertex
    Returns:
        list of vertices in DFS order
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Add neighbors in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph.adj_list.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result

def has_cycle(graph):
    """
    Detect cycle in a directed graph using DFS
    Args:
        graph: Graph object with adjacency list
    Returns:
        True if cycle exists, False otherwise
    """
    visited = set()
    rec_stack = set()

    def dfs_cycle(vertex):
        visited.add(vertex)
        rec_stack.add(vertex)

        for neighbor in graph.adj_list.get(vertex, []):
            if neighbor not in visited:
                if dfs_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(vertex)
        return False

    for vertex in range(graph.V):
        if vertex not in visited:
            if dfs_cycle(vertex):
                return True

    return False

def has_cycle_undirected(graph):
    """
    Detect cycle in an undirected graph using DFS
    Args:
        graph: Graph object with adjacency list
    Returns:
        True if cycle exists, False otherwise
    """
    visited = set()

    def dfs_cycle(vertex, parent):
        visited.add(vertex)

        for neighbor in graph.adj_list.get(vertex, []):
            if neighbor not in visited:
                if dfs_cycle(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True

        return False

    for vertex in range(graph.V):
        if vertex not in visited:
            if dfs_cycle(vertex, -1):
                return True

    return False
