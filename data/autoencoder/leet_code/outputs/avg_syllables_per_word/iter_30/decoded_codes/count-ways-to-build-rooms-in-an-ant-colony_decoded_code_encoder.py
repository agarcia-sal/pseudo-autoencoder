from math import comb

class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)
        graph = [[] for _ in range(n)]
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
                # Multiply by ways and by the combination of placing child's rooms among current rooms
                total_ways = (total_ways * ways * comb(current_size + size - 1, size)) % MOD
                current_size += size

            return total_ways, total_size

        return dp(0)[0]