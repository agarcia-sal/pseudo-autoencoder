from collections import defaultdict
from math import comb

class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)
        graph = defaultdict(list)
        for room in range(1, n):
            graph[prevRoom[room]].append(room)

        def dp(node: int) -> tuple[int, int]:
            children = graph[node]
            if not children:
                return 1, 1  # ways, size

            total_ways = 1
            total_size = 1  # counting current node
            child_results = []
            for child in children:
                ways, size = dp(child)
                child_results.append((ways, size))
                total_size += size

            current_size = 1
            for ways, size in child_results:
                combination_result = comb(current_size + size - 1, size) % MOD
                total_ways = (total_ways * combination_result) % MOD
                total_ways = (total_ways * ways) % MOD
                current_size += size

            return total_ways, total_size

        return dp(0)[0]