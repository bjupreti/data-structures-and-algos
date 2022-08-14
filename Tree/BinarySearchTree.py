from itertools import count


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return # node already exist
        
        if data < self.data:
            # Add data to the left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
                
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # search left tree
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            # search right tree
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
            
        elements.append(self.data)
            
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
            
        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()
            
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    # def delete(self, val):
    #     if val < self.data:
    #         if self.left:
    #             self.delete(self.left)
    #     elif val > self.data:
    #         if self.right:
    #             self.delete(self.right)
    #     else:
    #         if self.left is None and self.right is None:
    #             return None
    #         if self.left is None:
    #             return self.right
    #         if self.right is None:
    #             return self.left
            
    #         self.data = self.right
            
def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root
        
# bst = BinarySearchTree(30)
#     #         30
#     #         /\
#     #     20              39
#     #     /\              /\
#     # 10        25      35    42 
#     # /\         /\
#     #    15     23  
# bst.add_child(20)
# bst.add_child(39)
# bst.add_child(10)
# bst.add_child(25)
# bst.add_child(15)
# bst.add_child(23)
# bst.add_child(35)
# bst.add_child(42)

# print(bst.search(31))

if __name__ == "__main__":
    elements = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(elements)
    
    print("UK is in the list?", country_tree.search("UK"))
    print("Sweden is in the list?", country_tree.search("Sweden"))
    
    numbers_tree = build_tree([30, 20, 39, 10, 25, 35, 42, 15, 23])
    print("In order traversal gives this sorted list: ", numbers_tree.in_order_traversal())
    print("Post Order traversal", numbers_tree.post_order_traversal())
    print("Pre Order traversal", numbers_tree.pre_order_traversal())
    print("Max Number: ", numbers_tree.find_max())
    print("Min Number: ", numbers_tree.find_min())
    print("Sum: ", numbers_tree.calculate_sum())
    # print("After deleting 20:", numbers_tree.delete(20))