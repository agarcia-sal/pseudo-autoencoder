from collections import defaultdict
from typing import List, Tuple

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)

        # dp[i][j] will store a tuple (cost, path) representing minimal cost
        # and corresponding path for targetPath[:i+1] ending at node j.
        dp = [[(float('inf'), []) for _ in range(n)] for _ in range(m)]

        # Initialize for i == 0
        for j in range(n):
            cost = 0 if names[j] == targetPath[0] else 1
            dp[0][j] = (cost, [j])

        for i in range(1, m):
            for j in range(n):
                min_cost = float('inf')
                min_path = []
                for k in graph[j]:
                    prev_cost, prev_path = dp[i-1][k]
                    if prev_cost < min_cost:
                        min_cost = prev_cost
                        min_path = prev_path
                current_cost = min_cost + (0 if names[j] == targetPath[i] else 1)
                dp[i][j] = (current_cost, min_path + [j])

        min_cost = float('inf')
        min_path = []
        for j in range(n):
            cost, path = dp[m-1][j]
            if cost < min_cost:
                min_cost = cost
                min_path = path

        return min_path