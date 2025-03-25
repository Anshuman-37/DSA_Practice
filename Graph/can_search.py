from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # n = len(arr)
        # graph = {i: [] for i in range(n)}
        # for i in range(n):
        #     jump_forward = i + arr[i]
        #     jump_back = i - arr[i]
        #     # Adjust conditions to include index 0
        #     if jump_forward < n and jump_forward >= 0:
        #         graph[i].append(jump_forward)
        #     if jump_back < n and jump_back >= 0:
        #         graph[i].append(jump_back)

        # # Initialize the queue with the start index
        # queue = deque([start])
        # visited = set()

        # while queue:
        #     curr_index = queue.popleft()
        #     # Check if we've reached a 0 valued index
        #     if arr[curr_index] == 0:
        #         return True
        #     visited.add(curr_index)
        #     # Add all unvisited neighbors
        #     for neighbor in graph[curr_index]:
        #         if neighbor not in visited:
        #             queue.append(neighbor)
        # return False
        # Without making a graph DS
        n = len(arr)
        queue = deque([start])
        visited = set()

        while queue:
            i = queue.popleft()
            # Check if the current index has a value of 0
            if arr[i] == 0:
                return True

            # Mark the index as visited
            visited.add(i)

            # Calculate neighbors directly
            next_positions = [i + arr[i], i - arr[i]]
            for next_index in next_positions:
                if 0 <= next_index < n and next_index not in visited:
                    queue.append(next_index)

        return False
