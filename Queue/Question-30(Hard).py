from collections import deque

class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.response_time = 0
        self.waiting_time = 0
        self.in_queue_since = 0

class MLFQScheduler:
    def __init__(self, num_queues, time_quantums):
        self.num_queues = num_queues
        self.time_quantums = time_quantums
        self.queues = [deque() for _ in range(num_queues)]
        self.processes = {}
        self.current_time = 0
        self.completed_processes = []

    def add_process(self, process_id, arrival_time, burst_time):
        process = Process(process_id, arrival_time, burst_time)
        self.processes[process_id] = process
        self.queues[0].append(process_id)
        process.in_queue_since = arrival_time

    def get_next_process(self):
        for i in range(self.num_queues):
            if self.queues[i]:
                return i, self.queues[i][0]
        return -1, None

    def run(self):
        while self.processes or any(self.queues):
            for pid, process in list(self.processes.items()):
                if process.arrival_time <= self.current_time and pid not in [p for q in self.queues for p in q]:
                    self.queues[0].append(pid)
                    process.in_queue_since = self.current_time

            queue_index, current_process_id = self.get_next_process()

            if current_process_id is None:
                self.current_time += 1
                continue

            current_process = self.processes[current_process_id]

            if current_process.start_time == 0:
                current_process.start_time = self.current_time
                current_process.response_time = self.current_time - current_process.arrival_time

            time_slice = min(self.time_quantums[queue_index], current_process.remaining_time)

            for _ in range(time_slice):
                self.current_time += 1
                current_process.remaining_time -= 1

                for pid, process in list(self.processes.items()):
                    if process.arrival_time == self.current_time and pid not in [p for q in self.queues for p in q]:
                        self.queues[0].append(pid)
                        process.in_queue_since = self.current_time

            if current_process.remaining_time == 0:
                current_process.completion_time = self.current_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                self.completed_processes.append(current_process)
                self.queues[queue_index].popleft()
                del self.processes[current_process_id]
            else:
                self.queues[queue_index].popleft()
                if queue_index < self.num_queues - 1:
                    self.queues[queue_index + 1].append(current_process_id)
                    current_process.in_queue_since = self.current_time
                else:
                    self.queues[queue_index].append(current_process_id)
                    current_process.in_queue_since = self.current_time

        return self.completed_processes

if __name__ == "__main__":
    num_queues = 3
    time_quantums = [4, 8, float('inf')]

    scheduler = MLFQScheduler(num_queues, time_quantums)

    processes_data = [
        (1, 0, 20),
        (2, 0, 5),
        (3, 10, 30),
        (4, 12, 10)
    ]

    for pid, arrival, burst in processes_data:
        scheduler.add_process(pid, arrival, burst)

    completed_processes = scheduler.run()

    print("Process Scheduling Order:")
    for process in completed_processes:
        print(f"Process {process.process_id}: Arrival={process.arrival_time}, Burst={process.burst_time}, Start={process.start_time}, Completion={process.completion_time}, Response={process.response_time}, Waiting={process.waiting_time}, Turnaround={process.turnaround_time}")

    if completed_processes:
        avg_response_time = sum(p.response_time for p in completed_processes) / len(completed_processes)
        avg_waiting_time = sum(p.waiting_time for p in completed_processes) / len(completed_processes)
        avg_turnaround_time = sum(p.turnaround_time for p in completed_processes) / len(completed_processes)

        print("\nAverage Metrics:")
        print(f"Average Response Time: {avg_response_time:.2f}")
        print(f"Average Waiting Time: {avg_waiting_time:.2f}")
        print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")