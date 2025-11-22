import math
from typing import List, Dict, Set


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.size = [1] * size

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
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
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)
        uf = UnionFind(max_num + 1)
        prime_to_index: Dict[int, int] = {}

        for num in nums:
            for prime in self.prime_factors(num):
                if prime in prime_to_index:
                    uf.union(prime_to_index[prime], num)
                else:
                    prime_to_index[prime] = num

        max_component_size = 0
        for num in nums:
            root = uf.find(num)
            if uf.size[root] > max_component_size:
                max_component_size = uf.size[root]

        return max_component_size

    def prime_factors(self, n: int) -> Set[int]:
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2

        limit = int(math.isqrt(n)) + 1
        i = 3
        while i < limit and n > 1:
            while n % i == 0:
                factors.add(i)
                n //= i
                limit = int(math.isqrt(n)) + 1
            i += 2

        if n > 2:
            factors.add(n)

        return factors