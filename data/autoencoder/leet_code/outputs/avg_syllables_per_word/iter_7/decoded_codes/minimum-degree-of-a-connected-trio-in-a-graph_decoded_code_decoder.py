from typing import List, Set, Dict

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph: Dict[int, Set[int]] = {i: set() for i in range(1, n+1)}

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = float('inf')
        trio_found = False

        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if j not in graph[i]:
                    continue
                for k in range(j+1, n+1):
                    if k in graph[i] and k in graph[j]:
                        trio_found = True
                        trio_degree = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                        if trio_degree < min_degree:
                            min_degree = trio_degree

        return min_degree if trio_found else -1