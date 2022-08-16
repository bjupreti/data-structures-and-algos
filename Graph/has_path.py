from collections import deque

graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

def has_path_breadth_first(graph, src, dest):
    queue = deque()
    queue.appendleft(src)
    
    while queue:
        current = queue.pop()
        if current == dest:
            return True
        for neighbor in graph[current]:
            queue.appendleft(neighbor)
    return False

# def has_path_depth_first(graph, src, dest):
#     stack = deque()
#     stack.append(src)
    
#     while stack:
#         current = stack.pop()
#         if current == dest:
#             return True
#         for neighbor in graph[current]:
#             stack.append(neighbor)
#     return False

def has_path_depth_first(graph, src, dest):
    if src == dest:
        return True
    
    for neighbor in graph[src]:
        if has_path_depth_first(graph, neighbor, dest) is True:
            return True
    
    return False
    


print(has_path_breadth_first(graph, 'f', 'k'))
print(has_path_depth_first(graph, 'f', 'k'))