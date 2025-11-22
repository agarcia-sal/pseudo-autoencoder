from collections import deque, defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque()
        for index in range(n):
            if in_degree[index] == 0:
                queue.append(index)

        dp = [[0] * 26 for _ in range(n)]
        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            c_index = ord(colors[node]) - ord('a')
            dp[node][c_index] += 1
            if dp[node][c_index] > max_color_value:
                max_color_value = dp[node][c_index]
            visited += 1

            for neighbor in graph[node]:
                for c in range(26):
                    if dp[node][c] > dp[neighbor][c]:
                        dp[neighbor][c] = dp[node][c]
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return max_color_value if visited == n else -1