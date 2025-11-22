from collections import defaultdict
from math import comb

MOD = 10**9 + 7

class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        n = len(prevRoom)
        graph = defaultdict(list)
        # Build adjacency list from prevRoom
        for room in range(1, n):
            graph[prevRoom[room]].append(room)

        def dp(node: int) -> tuple[int, int]:
            children = graph[node]
            if not children:
                # Leaf node: Only one way and size 1
                return 1, 1

            total_ways = 1
            total_size = 1
            child_results = []
            for child in children:
                ways, size = dp(child)
                child_results.append((ways, size))
                total_size += size

            current_size = 1
            for ways, size in child_results:
                # Multiply ways by combination and ways from child under modulo
                total_ways *= comb(current_size + size - 1, size) * ways
                total_ways %= MOD
                current_size += size

            return total_ways, total_size

        return dp(0)[0]