edges = [
    [1, 2],
    [4, 6],
    [5, 6],
    [6, 7],
    [6, 8],
    [3, 10]
]

def build_graph(edges):
    graph = {}
    for a, b in edges:
        if a in graph: graph[a].append(b)
        else: graph[a] = [b]
        
        if b in graph: graph[b].append(a)
        else: graph[b] = [a]
    return graph

graph = build_graph(edges)
def connected_component_count(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited) is True:
            count += 1
    return count
        
def explore(graph, current, visited):
    if current in visited: return False
    
    visited.add(current)
    
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True
        
print(connected_component_count(graph))