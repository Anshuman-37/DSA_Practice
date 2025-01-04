# Question 8: Reverse the first k elements of a queue.
from collections import deque

def reverse_first_k_elements(queue, k):
    if not queue or k <= 0 or k > len(queue):
        return queue

    stack = []
    for _ in range(k):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

    return queue


my_queue = deque([1, 2, 3, 4, 5])
k_value = 3
reversed_queue = reverse_first_k_elements(my_queue, k_value)
print(f"Original Queue: {deque([1, 2, 3, 4, 5])}")
print(f"Queue after reversing first {k_value} elements: {reversed_queue}")

my_queue_2 = deque([10, 20, 30, 40, 50, 60])
k_value_2 = 4
reversed_queue_2 = reverse_first_k_elements(my_queue_2, k_value_2)
print(f"Original Queue: {deque([10, 20, 30, 40, 50, 60])}")
print(f"Queue after reversing first {k_value_2} elements: {reversed_queue_2}")

my_queue_3 = deque([100, 200])
k_value_3 = 2
reversed_queue_3 = reverse_first_k_elements(my_queue_3, k_value_3)
print(f"Original Queue: {deque([100, 200])}")
print(f"Queue after reversing first {k_value_3} elements: {reversed_queue_3}")
