from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

    #         a
    #         /\
    #   b         c
    #   /\        \
    #  e  d        e
    
def breadthFirstValues(root):
    """
    Prints and returns breadthFirstValues
    """
    if root is None: return []
    result = []
    queue = deque()
    queue.appendleft(root)
    
    while queue:
        current = queue.pop()
        result.append(current.data)
        
        if current.left: queue.appendleft(current.left)
        if current.right: queue.appendleft(current.right)
        
    print(result)
    return result


if __name__ == "__main__":
    breadthFirstValues(a)