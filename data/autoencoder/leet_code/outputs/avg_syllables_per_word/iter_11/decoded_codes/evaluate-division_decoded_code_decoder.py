class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}
        for (variable_a, variable_b), value in zip(equations, values):
            if variable_a not in graph:
                graph[variable_a] = {}
            if variable_b not in graph:
                graph[variable_b] = {}
            graph[variable_a][variable_b] = value
            graph[variable_b][variable_a] = 1 / value

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
            visited = set()
            result = dfs(start, end, visited)
            results.append(result)

        return results