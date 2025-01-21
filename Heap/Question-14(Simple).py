# Question 14: Reorganize a string so no two adjacent characters are the same using a max-heap.
import heapq
from collections import Counter

def reorganize_string(s):
    counts = Counter(s)
    max_heap = [(-count, char) for char, count in counts.items()]
    heapq.heapify(max_heap)

    result = ""
    previous_char = None
    previous_count = 0

    while max_heap:
        current_count, current_char = heapq.heappop(max_heap)
        result += current_char

        if previous_char and -previous_count > 0:
            heapq.heappush(max_heap, (previous_count, previous_char))

        previous_char = current_char
        previous_count = current_count + 1 # Decrement frequency (negated value)

    return result if len(result) == len(s) else ""

s = "aab"
reorganized_s = reorganize_string(s)
print(f"Reorganized string of '{s}': {reorganized_s}")

s = "aaab"
reorganized_s = reorganize_string(s)
print(f"Reorganized string of '{s}': {reorganized_s}")

s = "vvvlo"
reorganized_s = reorganize_string(s)
print(f"Reorganized string of '{s}': {reorganized_s}")