from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        # Iterate through the edges and probabilities
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        # prob[i] will store the maximum probability to reach node i from start
        prob = [0.0] * n
        prob[start] = 1.0

        # Max-heap (store negative probabilities because heapq is a min-heap)
        heap = [(-1.0, start)]

        while heap:
            # Get the node with the current highest probability
            curr_prob, node = heappop(heap)
            curr_prob = -curr_prob  # Convert back to positive

            # Early exit if we reached the end node
            if node == end:
                return curr_prob

            # If we already have a better probability for this node, skip it
            if curr_prob < prob[node]:
                continue

            # Traverse neighbors
            for neighbor, p in graph[node]:
                new_prob = curr_prob * p
                # Only update if this path gives a higher probability
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heappush(heap, (-new_prob, neighbor))

        # If the end node is unreachable, return 0.0
        return 0.0
