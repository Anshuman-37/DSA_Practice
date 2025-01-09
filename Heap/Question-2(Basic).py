#  Question 2: Build a min-heap from an array.
def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)
    return arr

array = [4, 10, 3, 5, 1]
min_heap = build_min_heap(array)
print(f"Original array: {array}")
print(f"Min-heap: {min_heap}")

array2 = [12, 11, 13, 5, 6, 7]
min_heap2 = build_min_heap(array2)
print(f"\nOriginal array: {array2}")
print(f"Min-heap: {min_heap2}")

array3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
min_heap3 = build_min_heap(array3)
print(f"\nOriginal array: {array3}")
print(f"Min-heap: {min_heap3}")

array4 = []
min_heap4 = build_min_heap(array4)
print(f"\nOriginal array: {array4}")
print(f"Min-heap: {min_heap4}")
