from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        graph = self.INITIALIZE_GRAPH(n, edges)
        degree = self.INITIALIZE_DEGREE_ARRAY(n)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = self.INITIALIZE_LEAVES(degree, n)

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return self.CONVERT_TO_LIST(leaves)

    def INITIALIZE_GRAPH(self, n: int, edges: list[list[int]]) -> dict[int, list[int]]:
        return defaultdict(list)

    def INITIALIZE_DEGREE_ARRAY(self, n: int) -> list[int]:
        return [0] * n

    def INITIALIZE_LEAVES(self, degree: list[int], n: int) -> deque[int]:
        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
        return leaves

    def CONVERT_TO_LIST(self, deque_structure: deque[int]) -> list[int]:
        return list(deque_structure)