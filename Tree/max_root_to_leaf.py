class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        

bt = Node(5)

bt.left = Node(11)
bt.left.left = Node(4)
bt.left.right = Node(2) 

bt.right = Node(3)
bt.right.right = Node(1)

count = 0
def maxPathSum(root):
    if root is None: return float('-inf')
    if root.left is None and root.right is None: return root.data
    
    maxChildPathSum = max(maxPathSum(root.left),maxPathSum(root.right))
    return root.data + maxChildPathSum


print(maxPathSum(bt))

