# Question 30: Implement a schedule manager that picks the shortest processing job next using a min-heap.
import heapq

class Job:
    def __init__(self, job_id, processing_time):
        self.job_id = job_id
        self.processing_time = processing_time

    def __lt__(self, other):
        return self.processing_time < other.processing_time

class ScheduleManager:
    def __init__(self):
        self.job_queue = []

    def add_job(self, job):
        heapq.heappush(self.job_queue, job)

    def get_next_job(self):
        if self.job_queue:
            return heapq.heappop(self.job_queue)
        return None

scheduler = ScheduleManager()
scheduler.add_job(Job("Job1", 5))
scheduler.add_job(Job("Job2", 2))
scheduler.add_job(Job("Job3", 8))
scheduler.add_job(Job("Job4", 1))

next_job = scheduler.get_next_job()
while next_job:
    print(f"Processing job: {next_job.job_id} with processing time: {next_job.processing_time}")
    next_job = scheduler.get_next_job()