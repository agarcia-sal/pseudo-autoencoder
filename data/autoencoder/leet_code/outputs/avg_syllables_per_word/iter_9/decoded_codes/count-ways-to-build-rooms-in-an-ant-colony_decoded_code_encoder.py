from math import comb

MOD = 10**9 + 7

class Solution:
    def waysToBuildRooms(self, prevRoom):
        n = len(prevRoom)
        graph = [[] for _ in range(n)]
        for room in range(1, n):
            graph[prevRoom[room]].append(room)

        def dp(node):
            if not graph[node]:
                return 1, 1

            total_ways = 1
            total_size = 1
            child_results = []
            for child in graph[node]:
                ways, size = dp(child)
                child_results.append((ways, size))
                total_size += size

            current_size = 1
            for ways, size in child_results:
                total_ways = (total_ways * comb(current_size + size - 1, size) * ways) % MOD
                current_size += size

            return total_ways, total_size

        return dp(0)[0]