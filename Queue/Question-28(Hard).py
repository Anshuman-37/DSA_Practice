#  Question 28: Find the minimum time for all processes to complete using round-robin scheduling.
from collections import deque

def min_completion_time_round_robin(burst_times, time_quantum):
    n = len(burst_times)
    remaining_burst_times = list(burst_times)
    queue = deque(range(n))
    current_time = 0

    while queue:
        process_index = queue.popleft()
        if remaining_burst_times[process_index] > 0:
            execution_time = min(remaining_burst_times[process_index], time_quantum)
            current_time += execution_time
            remaining_burst_times[process_index] -= execution_time
            if remaining_burst_times[process_index] > 0:
                queue.append(process_index)

    return current_time

if __name__ == "__main__":
    burst_times = [10, 5, 8]
    time_quantum = 2
    min_time = min_completion_time_round_robin(burst_times, time_quantum)
    print(f"Minimum completion time for burst times {burst_times} with time quantum {time_quantum}: {min_time}")

    burst_times = [4, 1, 3]
    time_quantum = 1
    min_time = min_completion_time_round_robin(burst_times, time_quantum)
    print(f"Minimum completion time for burst times {burst_times} with time quantum {time_quantum}: {min_time}")

    burst_times = [3, 1, 6, 4]
    time_quantum = 3
    min_time = min_completion_time_round_robin(burst_times, time_quantum)
    print(f"Minimum completion time for burst times {burst_times} with time quantum {time_quantum}: {min_time}")
