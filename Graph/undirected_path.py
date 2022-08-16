edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]

def buildGraph(edges):
    graph = {}
    for a, b in edges:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
            
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
    return graph
        
def undirectedPath(edges, src, dest):
    graph = buildGraph(edges)
    return has_path(graph, src, dest, set())

def has_path(graph, src, dest, visited):
    if src in visited: return False
    
    if src == dest:
        return True
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dest, visited) is True:
            return True
    
    return False
    
    
    
print(undirectedPath(edges, 'i', 'o'))
print(undirectedPath(edges, 'i', 'l'))