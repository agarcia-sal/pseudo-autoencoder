from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        number_of_nodes = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * number_of_nodes

        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        queue = deque(i for i in range(number_of_nodes) if in_degree[i] == 0)
        dp = [[0] * 26 for _ in range(number_of_nodes)]
        visited = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            node_color_index = ord(colors[node]) - ord('a')
            dp[node][node_color_index] += 1
            max_color_value = max(max_color_value, dp[node][node_color_index])
            visited += 1

            for neighbor in graph[node]:
                for color_index in range(26):
                    if dp[neighbor][color_index] < dp[node][color_index]:
                        dp[neighbor][color_index] = dp[node][color_index]
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return max_color_value if visited == number_of_nodes else -1