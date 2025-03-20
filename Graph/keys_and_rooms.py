from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = {i: rooms[i] for i in range(len(rooms))}

        # Initialize a deque for BFS starting with room 0
        queue = deque([0])
        visited = set()

        while queue:
            room_number = queue.popleft()
            if room_number not in visited:
                visited.add(room_number)
                # For each key (room number) in the current room, add it to the queue if not visited
                for key in graph[room_number]:
                    if key not in visited:
                        queue.append(key)

        # Return True if we visited all rooms
        return len(visited) == len(rooms)



