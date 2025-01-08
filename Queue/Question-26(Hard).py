# Question 26: Merge multiple queues of tasks into one while maintaining order.
from collections import deque
import heapq

def merge_sorted_queues(queues):
    merged_queue = deque()
    heap = []

    for i, q in enumerate(queues):
        if q:
            heapq.heappush(heap, (q[0], i))
            q.popleft()

    while heap:
        smallest_item, source_queue_index = heapq.heappop(heap)
        merged_queue.append(smallest_item)

        if queues[source_queue_index]:
            heapq.heappush(heap, (queues[source_queue_index][0], source_queue_index))
            queues[source_queue_index].popleft()

    return merged_queue

if __name__ == "__main__":
    queue1 = deque([1, 3, 5, 7])
    queue2 = deque([2, 4, 6])
    queue3 = deque([0, 8, 9, 10])
    queue4 = deque()

    multiple_queues = [queue1, queue2, queue3, queue4]
    merged = merge_sorted_queues(multiple_queues)
    print("Merged Sorted Queue:", list(merged))

    queue5 = deque([1, 2, 2, 5])
    queue6 = deque([2, 3, 4])
    multiple_queues2 = [queue5, queue6]
    merged2 = merge_sorted_queues(multiple_queues2)
    print("Merged Sorted Queue 2:", list(merged2))