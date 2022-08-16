from collections import deque

# def depth_first_print(graph, source):
#     stack = deque()
#     stack.append(source)
    
#     while stack:
#         current = stack.pop()
#         print(current)
#         for neighbor in graph[current]:
#             stack.append(neighbor)
     
def depth_first_print(graph, source):
    print(source)
    for neighbour in graph[source]:
        depth_first_print(graph, neighbour)
        
def breadth_first_print(graph, source):
    queue = deque()
    queue.appendleft(source)
    
    while queue:
        current = queue.pop()
        print(current)
        for neighbor in graph[current]:
            queue.appendleft(neighbor)
    
graph = {
    "a": ['c', 'b'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}

depth_first_print(graph, 'a')
breadth_first_print(graph, 'a')