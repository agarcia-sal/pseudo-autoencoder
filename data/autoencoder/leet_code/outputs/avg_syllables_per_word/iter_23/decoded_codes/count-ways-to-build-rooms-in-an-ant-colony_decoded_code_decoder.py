from math import comb
from collections import defaultdict
from typing import List, Tuple

MOD = 10**9 + 7

class Solution:  
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        graph = defaultdict(list)  # key -> list of child rooms

        for room in range(1, n):
            parent = prevRoom[room]
            graph[parent].append(room)

        def dp(node: int) -> Tuple[int, int]:
            if not graph[node]:
                return 1, 1  # ways, size

            total_ways = 1
            total_size = 1
            child_results = []

            for child in graph[node]:
                ways, size = dp(child)
                child_results.append((ways, size))
                total_size += size

            current_size = 1
            for ways, size in child_results:
                # Calculate combinations and multiply ways, modulo MOD
                total_ways = (total_ways * comb(current_size + size - 1, size) * ways) % MOD
                current_size += size

            return total_ways, total_size

        return dp(0)[0]