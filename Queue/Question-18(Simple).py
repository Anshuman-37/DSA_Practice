# Question 198: Reverse a queue using recursion.
from collections import deque

def reverse_queue_recursive(queue):
    if not queue:
        return
    front = queue.popleft()
    reverse_queue_recursive(queue)
    queue.append(front)

my_queue = deque([1, 2, 3, 4, 5])
print("Original Queue:", list(my_queue))

reverse_queue_recursive(my_queue)
print("Reversed Queue:", list(my_queue))

my_queue2 = deque(['a', 'b', 'c'])
print("Original Queue:", list(my_queue2))
reverse_queue_recursive(my_queue2)
print("Reversed Queue:", list(my_queue2))

my_queue3 = deque()
print("Original Queue:", list(my_queue3))
reverse_queue_recursive(my_queue3)
print("Reversed Queue:", list(my_queue3))