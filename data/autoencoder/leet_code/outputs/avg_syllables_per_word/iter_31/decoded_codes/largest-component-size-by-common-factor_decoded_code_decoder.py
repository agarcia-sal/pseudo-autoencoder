from math import sqrt


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.size = [1] * size

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
                self.size[rootU] += self.size[rootV]
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
                self.size[rootV] += self.size[rootU]
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
                self.size[rootU] += self.size[rootV]


class Solution:
    def largestComponentSize(self, nums):
        if not nums:
            return 0

        max_num = max(nums)
        uf = UnionFind(max_num + 1)
        prime_to_index = {}

        for num in nums:
            for prime in self.prime_factors(num):
                if prime in prime_to_index:
                    uf.union(prime_to_index[prime], num)
                else:
                    prime_to_index[prime] = num

        max_component_size = 0
        visited = set()
        for num in nums:
            root = uf.find(num)
            if root not in visited:
                max_component_size = max(max_component_size, uf.size[root])
                visited.add(root)

        return max_component_size

    def prime_factors(self, n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2

        i = 3
        max_factor = int(sqrt(n)) + 1
        while i <= max_factor and n > 1:
            while n % i == 0:
                factors.add(i)
                n //= i
                max_factor = int(sqrt(n)) + 1
            i += 2

        if n > 2:
            factors.add(n)

        return factors