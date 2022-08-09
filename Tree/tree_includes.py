from collections import deque
class Node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        

bt = Node('a')

bt.left = Node('b')
bt.left.left = Node('d')
bt.left.right = Node('e')

bt.right = Node('c')
bt.right = Node('f')


def depth_first_tree_includes(root, target):
    if root is None: return False
    if root.data == target:
        return True
    
    return depth_first_tree_includes(root.left, target) or depth_first_tree_includes(root.right, target)
    


def breadth_first_tree_include(root, target):
    if root is None: return False
    queue = deque()
    queue.appendleft(root)
    
    while queue:
        current = queue.pop()
        if current.data == target:
            return True
        
        if current.left: queue.appendleft(current.left)
        if current.right: queue.appendleft(current.right)
        
    return False


print(depth_first_tree_includes(bt, 'e')) # True
print(depth_first_tree_includes(bt, 'g')) # False
print(depth_first_tree_includes(None, 'g')) # False
print(breadth_first_tree_include(bt, 'e')) # True
print(breadth_first_tree_include(bt, 'g')) # False
print(breadth_first_tree_include(None, 'g')) # False