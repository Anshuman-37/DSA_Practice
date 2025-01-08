
from collections import deque

def generate_gray_codes_queue(n):
    if n == 0:
        return [""]

    queue = deque(["0", "1"])

    for _ in range(1, n):
        size = len(queue)
        for _ in range(size):
            prefix_zero = queue.popleft()
            queue.append(f"0{prefix_zero}")

        temp_list = list(queue)
        for i in range(len(temp_list) - 1, -1, -1):
            queue.append(f"1{temp_list[i][1:]}")

    return list(queue)

n = 3
gray_codes = generate_gray_codes_queue(n)
print(f"{n}-bit Gray codes: {gray_codes}")

n = 0
gray_codes = generate_gray_codes_queue(n)
print(f"{n}-bit Gray codes: {gray_codes}")

n = 1
gray_codes = generate_gray_codes_queue(n)
print(f"{n}-bit Gray codes: {gray_codes}")

n = 2
gray_codes = generate_gray_codes_queue(n)
print(f"{n}-bit Gray codes: {gray_codes}")