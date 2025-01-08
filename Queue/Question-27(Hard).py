# Question 27: Simulate a call center with multiple agents using queues.
from collections import deque
import heapq
import random

class Call:
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.start_time = None
        self.end_time = None

class Agent:
    def __init__(self, id):
        self.id = id
        self.is_busy = False
        self.available_at = 0

class CallCenterSimulator:
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.agents = [Agent(i) for i in range(num_agents)]
        self.waiting_queue = deque()
        self.event_queue = []
        self.current_time = 0
        self.total_calls = 0
        self.completed_calls = 0
        self.total_wait_time = 0

    def add_call(self):
        self.total_calls += 1
        arrival_time = self.current_time
        call = Call(arrival_time)
        heapq.heappush(self.event_queue, (arrival_time, "call_arrival", call))

    def find_available_agent(self):
        for agent in self.agents:
            if not agent.is_busy and self.current_time >= agent.available_at:
                return agent
        return None

    def assign_call_to_agent(self, call, agent):
        agent.is_busy = True
        call.start_time = self.current_time
        processing_time = random.randint(3, 10)
        completion_time = self.current_time + processing_time
        agent.available_at = completion_time
        heapq.heappush(self.event_queue, (completion_time, "call_completion", (call, agent)))

    def run_simulation(self, num_calls, max_simulation_time=100):
        for _ in range(num_calls):
            self.add_call()
            self.current_time += random.uniform(0.5, 3)

        while self.event_queue and self.current_time <= max_simulation_time:
            event_time, event_type, data = heapq.heappop(self.event_queue)
            self.current_time = event_time

            if event_type == "call_arrival":
                call = data
                available_agent = self.find_available_agent()
                if available_agent:
                    self.assign_call_to_agent(call, available_agent)
                else:
                    self.waiting_queue.append(call)
                    print(f"{self.current_time:.2f}: Call arrived and put in waiting queue. Queue size: {len(self.waiting_queue)}")

            elif event_type == "call_completion":
                call, agent = data
                call.end_time = self.current_time
                self.completed_calls += 1
                wait_time = call.start_time - call.arrival_time if call.start_time else 0
                self.total_wait_time += wait_time
                agent.is_busy = False
                print(f"{self.current_time:.2f}: Call completed by agent {agent.id}. Wait time: {wait_time:.2f}")

                if self.waiting_queue:
                    next_call = self.waiting_queue.popleft()
                    self.assign_call_to_agent(next_call, agent)
                    print(f"{self.current_time:.2f}: Agent {agent.id} assigned waiting call.")

        print("\n--- Simulation Summary ---")
        print(f"Simulation End Time: {self.current_time:.2f}")
        print(f"Total Calls Arrived: {self.total_calls}")
        print(f"Completed Calls: {self.completed_calls}")
        if self.completed_calls > 0:
            average_wait_time = self.total_wait_time / self.completed_calls
            print(f"Average Wait Time: {average_wait_time:.2f}")
        else:
            print("No calls were completed.")
        print(f"Calls Left in Waiting Queue: {len(self.waiting_queue)}")

if __name__ == "__main__":
    num_agents = 3
    num_calls = 10
    simulator = CallCenterSimulator(num_agents)
    simulator.run_simulation(num_calls)