from collections import deque

class FirstUniqueOptimal:
    def __init__(self):
        self.counts = {}
        self.unique_queue = deque()

    def add(self, value: int) -> None:
        self.counts[value] = self.counts.get(value, 0) + 1
        if self.counts[value] == 1:
            self.unique_queue.append(value)

    def showFirstUnique(self) -> int:
        while self.unique_queue and self.counts[self.unique_queue[0]] > 1:
            self.unique_queue.popleft()

        if self.unique_queue:
            return self.unique_queue[0]
        else:
            return -1

firstUnique = FirstUniqueOptimal()
firstUnique.add(2)
print(firstUnique.showFirstUnique())
firstUnique.add(2)
print(firstUnique.showFirstUnique())
firstUnique.add(3)
print(firstUnique.showFirstUnique())
firstUnique.add(1)
print(firstUnique.showFirstUnique())
firstUnique.add(3)
print(firstUnique.showFirstUnique())