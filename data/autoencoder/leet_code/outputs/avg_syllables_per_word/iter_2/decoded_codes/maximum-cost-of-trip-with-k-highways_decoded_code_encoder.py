from collections import defaultdict

class Solution:
    def maximumCost(self, n, highways, k):
        graph = defaultdict(list)
        for city1, city2, toll in highways:
            graph[city1].append((city2, toll))
            graph[city2].append((city1, toll))

        max_cost = -1

        def dfs(city, visited, cost, highways_used):
            nonlocal max_cost
            if highways_used == k:
                max_cost = max(max_cost, cost)
                return
            for neighbor, toll in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited, cost + toll, highways_used + 1)
                    visited.remove(neighbor)

        for start_city in range(n):
            visited = set([start_city])
            dfs(start_city, visited, 0, 0)

        return max_cost