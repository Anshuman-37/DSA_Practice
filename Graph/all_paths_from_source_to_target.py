from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        results = []

        def backtrack(curr_node, path):
            # Reached target
            if curr_node == target:
                results.append(list(path))
                return
            # Keep calling backtrack on the new node that we found
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        # Initial Path is basically zero
        path = [0]
        backtrack(0, path)

        return results
