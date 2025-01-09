# Question 4: Extract the minimum element from a min-heap.

def heapify_down(min_heap, index):
    n = len(min_heap)
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < n and min_heap[left] < min_heap[smallest]:
        smallest = left

    if right < n and min_heap[right] < min_heap[smallest]:
        smallest = right

    if smallest != index:
        min_heap[index], min_heap[smallest] = min_heap[smallest], min_heap[index]
        heapify_down(min_heap, smallest)

def extract_min(min_heap):
    if not min_heap:
        return None

    if len(min_heap) == 1:
        return min_heap.pop()

    min_element = min_heap[0]
    last_element = min_heap.pop()
    min_heap[0] = last_element
    heapify_down(min_heap, 0)

    return min_element

min_heap = [2, 5, 8, 9, 11]
print(f"Original min-heap: {min_heap}")

min_val = extract_min(min_heap)
print(f"Extracted minimum: {min_val}")
print(f"Min-heap after extraction: {min_heap}")

min_val = extract_min(min_heap)
print(f"\nExtracted minimum: {min_val}")
print(f"Min-heap after extraction: {min_heap}")

min_heap2 = [1]
print(f"\nOriginal min-heap: {min_heap2}")
min_val2 = extract_min(min_heap2)
print(f"Extracted minimum: {min_val2}")
print(f"Min-heap after extraction: {min_heap2}")

min_heap3 = []
print(f"\nOriginal min-heap: {min_heap3}")
min_val3 = extract_min(min_heap3)
print(f"Extracted minimum: {min_val3}")
print(f"Min-heap after extraction: {min_heap3}")