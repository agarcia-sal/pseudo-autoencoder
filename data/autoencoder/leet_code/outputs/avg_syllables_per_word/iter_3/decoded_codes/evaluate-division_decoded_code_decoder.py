from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return weight * res
            visited.remove(start)
            return -1.0

        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))
        return results