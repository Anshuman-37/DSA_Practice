
from collections import deque

def interleave_queue_halves(queue):
    if not queue:
        return

    n = len(queue)
    if n % 2 != 0:
        raise ValueError("Queue length must be even to interleave halves")

    half_size = n // 2
    temp_queue = deque()

    for _ in range(half_size):
        temp_queue.append(queue.popleft())

    for _ in range(half_size):
        queue.append(temp_queue.popleft())
        queue.append(queue.popleft())

my_queue = deque([11, 12, 13, 14, 15, 16])
print("Original Queue:", my_queue)
interleave_queue_halves(my_queue)
print("Interleaved Queue:", my_queue)

my_queue_2 = deque([1, 2, 3, 4])
print("Original Queue:", my_queue_2)
interleave_queue_halves(my_queue_2)
print("Interleaved Queue:", my_queue_2)

try:
    my_queue_odd = deque([1, 2, 3, 4, 5])
    interleave_queue_halves(my_queue_odd)
except ValueError as e:
    print(e)