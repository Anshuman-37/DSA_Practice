# Question 191: Move all negative numbers to the front of a queue.
from collections import deque

def move_negatives_to_front(queue):

    if not queue:
        return

    negative_queue = deque()
    positive_queue = deque()

    while queue:
        element = queue.popleft()
        if element < 0:
            negative_queue.append(element)
        else:
            positive_queue.append(element)

    queue.extend(negative_queue)
    queue.extend(positive_queue)

my_queue = deque([1, -2, 3, -4, 5, -6])
print("Original Queue:", my_queue)
move_negatives_to_front(my_queue)
print("Queue with negatives at front:", my_queue)

my_queue_2 = deque([-5, -3, -1, 2, 4, 6])
print("Original Queue:", my_queue_2)
move_negatives_to_front(my_queue_2)
print("Queue with negatives at front:", my_queue_2)

my_queue_3 = deque([10, 20, 30, 40, 50])
print("Original Queue:", my_queue_3)
move_negatives_to_front(my_queue_3)
print("Queue with negatives at front:", my_queue_3)

my_queue_4 = deque([-1, -2, -3, -4, -5])
print("Original Queue:", my_queue_4)
move_negatives_to_front(my_queue_4)
print("Queue with negatives at front:", my_queue_4)

my_queue_5 = deque()
print("Original Queue:", my_queue_5)
move_negatives_to_front(my_queue_5)
print("Queue with negatives at front:", my_queue_5)