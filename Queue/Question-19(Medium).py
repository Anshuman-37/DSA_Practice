# Question 19: Given a queue of characters, remove all non-alphabets.
from collections import deque

def remove_non_alphabets(char_queue):
    alphabets_queue = deque()
    while char_queue:
        char = char_queue.popleft()
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            alphabets_queue.append(char)

    char_queue.clear()
    char_queue.extend(alphabets_queue)

my_queue = deque(['a', '1', 'B', '$', 'c', ' ', 'D', '9'])
print("Original Queue:", list(my_queue))

remove_non_alphabets(my_queue)
print("Queue after removing non-alphabets:", list(my_queue))

my_queue2 = deque(['!', '@', '#', '$', '%'])
print("Original Queue:", list(my_queue2))
remove_non_alphabets(my_queue2)
print("Queue after removing non-alphabets:", list(my_queue2))

my_queue3 = deque(['p', 'q', 'r', 's'])
print("Original Queue:", list(my_queue3))
remove_non_alphabets(my_queue3)
print("Queue after removing non-alphabets:", list(my_queue3))

my_queue4 = deque([])
print("Original Queue:", list(my_queue4))
remove_non_alphabets(my_queue4)
print("Queue after removing non-alphabets:", list(my_queue4))