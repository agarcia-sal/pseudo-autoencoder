from math import sqrt
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return False
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
        return True

class Solution:
    def gcdSort(self, nums):
        sorted_nums = sorted(nums)
        max_val = max(nums)
        uf = UnionFind(max_val + 1)
        for num in nums:
            limit = int(sqrt(num)) + 1
            for factor in range(2, limit):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)
        for i in range(len(nums)):
            if uf.find(nums[i]) != uf.find(sorted_nums[i]):
                return False
        return True