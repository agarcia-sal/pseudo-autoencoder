class Solution:
    def minTrioDegree(self, n, edges):
        graph = {i: set() for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = float('inf')
        for i in range(1, n + 1):
            for j in graph[i]:
                if j > i:
                    for k in graph[i]:
                        if k > j and k in graph[j]:
                            degree = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                            if degree < min_degree:
                                min_degree = degree

        return min_degree if min_degree != float('inf') else -1