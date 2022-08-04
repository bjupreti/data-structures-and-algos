from collections import deque

queue = deque()

queue.appendleft(1)
queue.appendleft(2)
queue.appendleft(3)

print(queue)

print(queue.pop())

print(queue)