# Question 197: Check if a queue can be sorted using a stack.
from collections import deque

def is_sortable_with_stack(queue):
    stack = []
    expected = 1

    while queue:
        front = queue[0]

        if front == expected:
            queue.popleft()
            expected += 1
        elif stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        elif stack and stack[-1] < front:
            return False
        else:
            stack.append(queue.popleft())

    while stack:
        if stack[-1] == expected:
            stack.pop()
            expected += 1
        else:
            return False

    return True

queue1 = deque([1, 2, 3])
print(f"Queue {list(queue1)} can be sorted: {is_sortable_with_stack(queue1)}")

queue2 = deque([3, 2, 1])
print(f"Queue {list(queue2)} can be sorted: {is_sortable_with_stack(queue2)}")

queue3 = deque([1, 3, 2])
print(f"Queue {list(queue3)} can be sorted: {is_sortable_with_stack(queue3)}")

queue4 = deque([3, 1, 2])
print(f"Queue {list(queue4)} can be sorted: {is_sortable_with_stack(queue4)}")

queue5 = deque([2, 1, 3])
print(f"Queue {list(queue5)} can be sorted: {is_sortable_with_stack(queue5)}")

queue6 = deque([2, 3, 1])
print(f"Queue {list(queue6)} can be sorted: {is_sortable_with_stack(queue6)}")
