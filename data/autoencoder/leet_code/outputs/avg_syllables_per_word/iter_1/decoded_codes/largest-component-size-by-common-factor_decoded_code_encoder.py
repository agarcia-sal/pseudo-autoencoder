import math

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.size_arr = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru != rv:
            if self.rank[ru] > self.rank[rv]:
                self.parent[rv] = ru
                self.size_arr[ru] += self.size_arr[rv]
            elif self.rank[ru] < self.rank[rv]:
                self.parent[ru] = rv
                self.size_arr[rv] += self.size_arr[ru]
            else:
                self.parent[rv] = ru
                self.rank[ru] += 1
                self.size_arr[ru] += self.size_arr[rv]

def prime_factors(n):
    f = {}
    while n % 2 == 0:
        f[2] = 1
        n //= 2
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            f[i] = 1
            n //= i
    if n > 2:
        f[n] = 1
    return f.keys()

def largestComponentSize(nums):
    uf = UnionFind(max(nums) + 1)
    prime_to_num = {}
    for num in nums:
        for p in prime_factors(num):
            if p in prime_to_num:
                uf.union(prime_to_num[p], num)
            else:
                prime_to_num[p] = num
    return max(uf.size_arr[uf.find(num)] for num in nums)