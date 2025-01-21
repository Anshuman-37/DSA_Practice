# Question 25: Design a data structure that supports insert, delete, and getMedian in O(log n) using heaps.
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (stores smaller half, negated values)
        self.large = []  # min-heap (stores larger half)
        self.deleted_small = set()
        self.deleted_large = set()

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def remove(self, num):
        if num in self.small_data():
            self.deleted_small.add(num)
        elif num in self.large_data():
            self.deleted_large.add(num)
        self._clean_heaps()

    def _clean_heaps(self):
        while self.small and -self.small[0] in self.deleted_small:
            self.deleted_small.remove(-self.small[0])
            heapq.heappop(self.small)
        while self.large and self.large[0] in self.deleted_large:
            self.deleted_large.remove(self.large[0])
            heapq.heappop(self.large)

    def small_data(self):
        return set(-x for x in self.small)

    def large_data(self):
        return set(self.large)

    def findMedian(self):
        self._clean_heaps()
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(f"Median: {medianFinder.findMedian()}")
medianFinder.addNum(3)
print(f"Median: {medianFinder.findMedian()}")
medianFinder.remove(2)
print(f"Median after removing 2: {medianFinder.findMedian()}")