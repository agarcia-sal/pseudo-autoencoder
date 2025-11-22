from collections import deque
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        queue = deque([[0]])
        ans = []
        while queue:
            path = queue.popleft()
            u = path[-1]
            if u == n - 1:
                ans.append(path)
                continue
            for v in graph[u]:
                queue.append(path + [v])
        return ans