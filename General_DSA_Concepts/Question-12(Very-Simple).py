import time
import sys
from datetime import datetime
from contextlib import contextmanager

@contextmanager
def timer(name):
    print(f"=== {name} ===")
    start_time = time.time()
    print(f"{name} started at {datetime.now()}")
    yield
    end_time = time.time()
    print(f"{name} finished at {datetime.now()}")
    print(f"Time taken: {end_time - start_time:.10f} seconds\n")

def factorial_iterative(n: int):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n: int):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    n = 97
    sys.set_int_max_str_digits(100000)
    sys.setrecursionlimit(100000)
    with timer("factorial_iterative"):
        iter_result = factorial_iterative(n)

    with timer("factorial_recursive"):
        rec_result = factorial_recursive(n)
