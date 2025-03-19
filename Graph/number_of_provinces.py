from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        number_of_components = 0
        visit = [False] * size
        def dfs(node, isConnected, visit):
            visit[node] = True
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visit[i]:
                    dfs(i, isConnected, visit)

        for i in range(size):
            if not visit[i]:
                number_of_components += 1
                dfs(i, isConnected, visit)
        return number_of_components