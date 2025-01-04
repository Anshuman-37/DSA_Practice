# Question 192: Check if two queues store the same elements in the same order.
from collections import deque

def are_queues_same(queue1, queue2):
    if len(queue1) != len(queue2):
        return False

    if not queue1:
        return True


    n = len(queue1)
    temp_queue2 = deque(queue2)

    for _ in range(n):
        if queue1[0] != temp_queue2[0]:
            return False
        queue1.append(queue1.popleft())
        temp_queue2.append(temp_queue2.popleft())

    return True

queue_a1 = deque([1, 2, 3])
queue_a2 = deque([1, 2, 3])
print(f"Queues {queue_a1} and {queue_a2} are the same: {are_queues_same(queue_a1, queue_a2)}")  # Output: True

queue_b1 = deque([1, 2, 3])
queue_b2 = deque([1, 3, 2])
print(f"Queues {queue_b1} and {queue_b2} are the same: {are_queues_same(queue_b1, queue_b2)}")  # Output: False

queue_c1 = deque([1, 2, 3])
queue_c2 = deque([1, 2])
print(f"Queues {queue_c1} and {queue_c2} are the same: {are_queues_same(queue_c1, queue_c2)}")  # Output: False

queue_d1 = deque([5,6,7,8,9,10])
queue_d2 = deque([10,9,8,7,6,5])
print(f"Queues {queue_d1} and {queue_d2} are the same: {are_queues_same(queue_d1, queue_d2)}")  # Output: True

queue_e1 = deque([1, 2, 3])
queue_e2 = deque([3, 1, 2])
print(f"Queues {queue_e1} and {queue_e2} are the same: {are_queues_same(queue_e1, queue_e2)}")  # Output: False