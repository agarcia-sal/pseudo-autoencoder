from collections import defaultdict
import math

class Solution:
    MOD = 10**9 + 7

    def waysToBuildRooms(self, previousRoom: list[int]) -> int:
        n = len(previousRoom)
        graph = defaultdict(list)
        for room in range(1, n):
            graph[previousRoom[room]].append(room)

        # Precompute factorials and inverse factorials for combinations
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % self.MOD

        inv_fact[n] = pow(fact[n], self.MOD - 2, self.MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % self.MOD

        def comb(a: int, b: int) -> int:
            if b > a or b < 0:
                return 0
            return fact[a] * inv_fact[b] % self.MOD * inv_fact[a - b] % self.MOD

        def dp(node: int) -> tuple[int, int]:
            children = graph[node]
            if not children:
                return 1, 1

            total_ways = 1
            total_size = 1
            child_results = []
            for child in children:
                ways, size = dp(child)
                child_results.append((ways, size))
                total_size += size

            curr_size = 1
            for ways, size in child_results:
                total_ways = total_ways * comb(curr_size + size - 1, size) % self.MOD
                total_ways = total_ways * ways % self.MOD
                curr_size += size

            return total_ways, total_size

        return dp(0)[0]