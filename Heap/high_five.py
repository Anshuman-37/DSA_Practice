from typing import List
from collections import defaultdict
import heapq


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_graph = defaultdict(list)
        for student, score in items:
            student_graph[student].append(score)

        res = []
        for student, scores in student_graph.items():
            top_five = heapq.nlargest(5, scores)
            average = sum(top_five) // 5
            res.append([student, average])

        return sorted(res)
