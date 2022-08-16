from collections import deque
edges = [
    ["w", "x"],
    ["w", "v"],
    ["x", "y"],
    ["y", "z"],
    ["v", "z"]
]

def build_graph(edges):
    graph = {}
    
    for a, b in edges:
        if a in graph: graph[a].append(b)
        else: graph[a] = [b] 
        
        if b in graph: graph[b].append(a)
        else: graph[b] = [a] 
    
    return graph

def shortest_path(edges, src, dest):
    graph = build_graph(edges)
    visited = {src}
    
    queue = deque()
    queue.appendleft((src, 0))

    while queue:
        current, distance = queue.pop()
        
        if current == dest:
            return distance
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.appendleft((neighbor, distance + 1))
                visited.add(neighbor)
        
    return -1
    

print(shortest_path(edges, 'w', 'z'))