from collections import defaultdict

class Solution:
    MOD = 10**9 + 7

    def waysToBuildRooms(self, prevRoom):
        n = len(prevRoom)
        graph = defaultdict(list)
        for room in range(1, n):
            graph[prevRoom[room]].append(room)

        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % self.MOD

        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], self.MOD - 2, self.MOD)
        for i in reversed(range(1, n)):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % self.MOD

        def comb(a, b):
            return (fact[a] * inv_fact[b] % self.MOD) * inv_fact[a - b] % self.MOD

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
                total_ways = total_ways * comb(current_size + size - 1, size) % self.MOD
                total_ways = total_ways * ways % self.MOD
                current_size += size

            return total_ways, total_size

        return dp(0)[0]