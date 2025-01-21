# Question 15: Find the median of a running stream of numbers using two heaps.
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
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