class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        
    def get_level(self):
        level = 0
        
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level
    
    def print_tree(self):
        spaces = "  " * self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(f"{prefix} {self.data}")
        if self.children:
            for child in self.children:
                child.print_tree()
            

root = TreeNode("Electronics")

mobile = TreeNode("Mobile")
root.add_child(mobile)
iphone = TreeNode("iPhone")
samsung = TreeNode("Samsung")
mobile.add_child(iphone)
mobile.add_child(samsung)

laptop = TreeNode("Laptop")
root.add_child(laptop)
acer = TreeNode("Acer")
hp = TreeNode("HP")
laptop.add_child(acer)
laptop.add_child(hp)

root.print_tree()
