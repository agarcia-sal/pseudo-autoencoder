class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        for (a, b), value in zip(equations, values):
            graph.setdefault(a, {})[b] = value
            graph.setdefault(b, {})[a] = 1 / value

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            visited.remove(start)
            return -1.0

        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))
        return results