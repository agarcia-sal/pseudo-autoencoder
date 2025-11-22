from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        out_degree = defaultdict(int)
        in_degree = defaultdict(int)

        for u, v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1

        start_node = None
        for node in graph:
            if out_degree[node] == in_degree[node] + 1:
                start_node = node
                break
        if start_node is None:
            start_node = next(iter(graph))

        path = []
        stack = [start_node]

        while stack:
            u = stack[-1]
            if graph[u]:
                v = graph[u].pop()
                stack.append(v)
            else:
                path.append(stack.pop())

        path.reverse()

        result = []
        for i in range(len(path) - 1):
            result.append([path[i], path[i + 1]])

        return result