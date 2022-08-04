# from collections import deque

# stack = deque()

# # print(dir(stack)) # show all the methods

# stack.append("https://www.cnn.com/1")
# stack.append("https://www.cnn.com/2")
# stack.append("https://www.cnn.com/3")

# print(stack)

# print(stack.pop())

# print(stack)


from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
        
    def pop(self):
        self.container.pop()
        
    def push(self, data):
        self.container.append(data)
        
    def peek(self):
        return self.container[-1]
        
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
history = Stack()
history.push("https://www.cnn.com/1")
history.push("https://www.cnn.com/2")
history.push("https://www.cnn.com/3")

print(history.size())

print(history.peek())

history.pop()

print(history.size())

print(history.peek())

history.pop()
history.pop()

print(history.is_empty())
