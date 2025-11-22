from math import inf

class Solution:
    def minTrioDegree(self, n: int, edges: list[list[int]]) -> int:
        graph = {i: set() for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = inf
        trio_found = False

        for i in range(1, n + 1):
            neighbors_i = graph[i]
            for j in range(i + 1, n + 1):
                if j in neighbors_i:
                    neighbors_j = graph[j]
                    for k in range(j + 1, n + 1):
                        if k in neighbors_i and k in neighbors_j:
                            trio_found = True
                            degree_i = len(neighbors_i)
                            degree_j = len(neighbors_j)
                            degree_k = len(graph[k])
                            trio_degree = degree_i + degree_j + degree_k - 6
                            if trio_degree < min_degree:
                                min_degree = trio_degree

        return min_degree if trio_found else -1