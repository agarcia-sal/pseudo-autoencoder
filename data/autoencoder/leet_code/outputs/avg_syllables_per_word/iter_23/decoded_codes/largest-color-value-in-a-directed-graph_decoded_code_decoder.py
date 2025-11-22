from collections import deque, defaultdict
from typing import List, Dict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph: Dict[int, List[int]] = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque(i for i in range(n) if in_degree[i] == 0)

        # dp[node][c] = max count of color c on a path ending at node
        dp = [[0] * 26 for _ in range(n)]
        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            c_index = ord(colors[node]) - ord('a')
            dp[node][c_index] += 1
            max_color_value = max(max_color_value, dp[node][c_index])
            visited += 1

            for neighbor in graph[node]:
                for c in range(26):
                    if dp[neighbor][c] < dp[node][c]:
                        dp[neighbor][c] = dp[node][c]
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if visited == n:
            return max_color_value
        else:
            return -1