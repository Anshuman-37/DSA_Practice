# Question 204: Implement a fixed-length queue that blocks when full (producer-consumer).
from collections import deque
import threading

class FixedBlockingQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def enqueue(self, item):
        with self.not_full:
            while len(self.queue) == self.capacity:
                self.not_full.wait()
            self.queue.append(item)
            self.not_empty.notify()

    def dequeue(self):
        with self.not_empty:
            while not self.queue:
                self.not_empty.wait()
            item = self.queue.popleft()
            self.not_full.notify()
            return item

    def qsize(self):
        with self.lock:
            return len(self.queue)

import time
import random

def producer(queue, items_to_produce):
    for i in range(items_to_produce):
        item = f"Item {i}"
        print(f"Producer: Enqueueing {item}")
        queue.enqueue(item)
        time.sleep(random.random() * 0.5)

def consumer(queue, items_to_consume):
    for _ in range(items_to_consume):
        item = queue.dequeue()
        print(f"Consumer: Dequeued {item}")
        time.sleep(random.random() * 0.5)

if __name__ == "__main__":
    queue_capacity = 5
    num_items = 10
    my_queue = FixedBlockingQueue(queue_capacity)

    producer_thread = threading.Thread(target=producer, args=(my_queue, num_items))
    consumer_thread = threading.Thread(target=consumer, args=(my_queue, num_items))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("Finished.")
