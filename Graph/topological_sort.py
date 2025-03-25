from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prereq in prereqs:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodes_visited = 0
        while q:
            node = q.popleft()
            nodes_visited += 1
            for neb in adj[node]:
                indegree[neb] -= 1
                if indegree[neb] == 0:
                    q.append(neb)

        return nodes_visited == numCourses
