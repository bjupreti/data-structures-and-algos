class Node:
    """Singly-linked node"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    """Singly-linked LinkedList"""
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def print(self):
        itr = self.head
        llstr = ""
        while itr:
            llstr += f"{itr.data}-->"
            itr = itr.next
        print(llstr)
        
    def insert_at_end(self, data):
        if self.head is None: 
            self.head = Node(data)
            return
            
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            
            count += 1
            itr = itr.next
        
        
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            count += 1
            itr = itr.next
        
    
    def insert_values(self, data_list):
        self.head = None
        
        for data in data_list:
            self.insert_at_end(data)
    
ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_end(3)
ll.print()
ll.insert_at(1, 4)
ll.print()
ll.remove_at(1)
ll.print()
# ll.insert_values([1,2,3,4,5])
ll.insert_values(['apple', 'ball', 'cat'])
ll.print()
print(ll.get_length())