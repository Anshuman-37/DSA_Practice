# Question 21: Check if a given sequence can be formed by a stack permutation.
from collections import deque


def is_stack_permutation(input_sequence, target_sequence):
    stack = []
    input_queue = deque(input_sequence)
    j = 0

    while input_queue:
        stack.append(input_queue.popleft())
        while stack and stack[-1] == target_sequence[j]:
            stack.pop()
            j += 1

    return j == len(target_sequence) and not stack


input_sequence = [1, 2, 3]
target_sequence1 = [2, 1, 3]
target_sequence2 = [3, 1, 2]

print(
    f"Is {target_sequence1} a stack permutation of {input_sequence}? {is_stack_permutation(input_sequence, target_sequence1)}")
print(
    f"Is {target_sequence2} a stack permutation of {input_sequence}? {is_stack_permutation(input_sequence, target_sequence2)}")
