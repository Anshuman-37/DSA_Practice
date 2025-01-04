# Question 189: Generate binary numbers from 1 to n using a queue.
from collections import deque

def generate_binary_numbers(n):
    if n <= 0:
        return []

    binary_numbers = []
    queue = deque(['1'])

    while len(binary_numbers) < n:
        current = queue.popleft()
        binary_numbers.append(current)

        s1 = current + '0'
        s2 = current + '1'

        queue.append(s1)
        if len(binary_numbers) < n:
            queue.append(s2)

    return binary_numbers

n = 5
result = generate_binary_numbers(n)
print(f"Binary numbers from 1 to {n}: {result}")

n = 10
result = generate_binary_numbers(n)
print(f"Binary numbers from 1 to {n}: {result}")