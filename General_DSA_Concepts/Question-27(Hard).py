# Question 27: Implement a thread-safe stack (consider synchronization).
import threading
from threading import Thread
import time

class ThreadSafeStack:
    """
    A thread-safe stack is a stack data structure designed to be safely accessed and manipulated by multiple threads
    concurrently without causing data corruption or inconsistent states. In a multi-threaded environment, two or more threads
    could attempt to push or pop elements at the same time, potentially leading to race conditions, deadlocks, or unexpected
    behavior if the access is not properly synchronized.

    To ensure thread safety, a thread-safe stack incorporates synchronization mechanisms that control how threads interact
    with the stack. Common approaches include using locks (such as mutexes) around operations to make sure only one thread
    can modify the stack’s internal data at a time, or employing lock-free algorithms that utilize atomic operations to
    manage concurrent access safely. With these measures in place, developers can rely on a thread-safe stack to behave
    correctly even when operations are performed by multiple threads simultaneously.
    """
    def __init__(self):
        self._stack = []
        self._lock =  threading.Lock()

    def push(self,x):
        with self._lock:
            self._stack.append(x)

    def pop(self):
        with self._lock:
            if not self._stack:
                return None
            return self._stack.pop()

    def is_empty(self):
        with self._lock:
            return len(self._stack).__eq__(0)

    def size(self):
        with self._lock:
            return len(self._stack)


def worker(stack, name, count):
    for i in range(count):
        stack.push(f"Item {i} from {name}")
        time.sleep(0.1)

if __name__ == "__main__":
    stack = ThreadSafeStack()

    threads = [
        Thread(target=worker, args=(stack, "Thread A", 5)),
        Thread(target=worker, args=(stack, "Thread B", 5))
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    while not stack.is_empty():
        print(stack.pop())


