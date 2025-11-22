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
                ways, size = dp(child)
                child_results.append((ways, size))
                total_size += size

            current_size = 1
            for ways, size in child_results:
                # Combination: ways to interleave the subtree positions
                comb_val = comb(current_size + size - 1, size)
                total_ways = (total_ways * comb_val * ways) % MOD
                current_size += size

            return total_ways, total_size

        return dp(0)[0]