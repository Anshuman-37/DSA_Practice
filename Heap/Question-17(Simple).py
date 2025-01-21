# Question 17: Connect ropes with minimum cost using a min-heap.
import heapq

def min_cost_to_connect_ropes(ropes):
    heapq.heapify(ropes)
    min_cost = 0

    while len(ropes) > 1:
        shortest1 = heapq.heappop(ropes)
        shortest2 = heapq.heappop(ropes)
        current_cost = shortest1 + shortest2
        min_cost += current_cost
        heapq.heappush(ropes, current_cost)

    return min_cost

ropes = [8, 4, 6, 12]
min_cost = min_cost_to_connect_ropes(ropes)
print(f"Minimum cost to connect ropes: {min_cost}")