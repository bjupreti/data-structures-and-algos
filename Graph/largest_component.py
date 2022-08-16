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

def largest_component(graph):
    largest = 0
    visited = set()
    for node in graph:
        count_of_component = exploreSize(graph, node, visited)
        if count_of_component > largest:
            largest = count_of_component
    return largest
        

def exploreSize(graph, current, visited):
    if current in visited: return 0
    
    visited.add(current)
    
    size = 1
    
    for node in graph[current]:
        size += exploreSize(graph, node, visited)
        
    return size

print(largest_component(graph))