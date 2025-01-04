# Question 1: Explain the concept of a queue and basic operations (enqueue, dequeue, peek).
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue[0])
print(queue.popleft())
print(queue.popleft())
print(queue)