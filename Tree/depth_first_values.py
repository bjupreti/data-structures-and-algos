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
    
def depthFirstValuesIterative(root = None):
    """
    Iterative Version of depthFirstValues
    Returns the values as well as print the values
    """
    if root is None: return []
    stack = deque()
    stack.append(root)
    
    result = []
    
    while stack:
        current = stack.pop()
        result.append(current.data)
        
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    print(result)  
    return result

def depthFirstValuesRecursive(root = None):
    if root is None: return []
    
    left = depthFirstValuesRecursive(root.left)  
    right = depthFirstValuesRecursive(root.right) 
    
    print([root.data] + left + right)
    return [root.data] + left + right
    
        
        
        
if __name__ == "__main__":
    depthFirstValuesIterative(a)
    depthFirstValuesRecursive(a)
    