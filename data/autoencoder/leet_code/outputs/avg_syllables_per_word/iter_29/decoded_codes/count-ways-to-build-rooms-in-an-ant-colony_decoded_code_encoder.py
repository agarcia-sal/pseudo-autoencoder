from collections import defaultdict
from math import comb

MOD = 10**9 + 7

class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        n = len(prevRoom)
        graph = defaultdict(list)
        for room in range(1, n):
            graph[prevRoom[room]].append(room)

        def dp(node: int) -> tuple[int, int]:
            if not graph[node]:
                return 1, 1

            total_ways = 1
            total_size = 1
            child_results = []
            for child in graph[node]:
                ways_size = dp(child)
                child_results.append(ways_size)
                total_size += ways_size[1]

            current_size = 1
            for ways, size in child_results:
                total_ways = (total_ways * comb(current_size + size - 1, size) * ways) % MOD
                current_size += size

            return total_ways, total_size

        return dp(0)[0]