from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node: int, parent: int, disc: List[int], low: List[int], time: List[int], graph: List[List[int]], critical: List[List[int]]) -> None:
            disc[node] = time[0]
            low[node] = time[0]
            time[0] += 1

            for neighbor in graph[node]:
                if disc[neighbor] == -1:
                    dfs(neighbor, node, disc, low, time, graph, critical)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        critical.append([node, neighbor])
                elif neighbor != parent:
                    low[node] = min(low[node], disc[neighbor])

        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [-1] * n

        time = [0]
        critical = []

        for node in range(n):
            if disc[node] == -1:
                dfs(node, -1, disc, low, time, graph, critical)

        return critical