class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
        if rp == rq:
            return False
        if self.rank[rp] > self.rank[rq]:
            self.parent[rq] = rp
        elif self.rank[rp] < self.rank[rq]:
            self.parent[rp] = rq
        else:
            self.parent[rq] = rp
            self.rank[rp] += 1
        return True

def gcdSort(nums):
    import math
    sorted_nums = sorted(nums)
    max_val = max(nums)
    uf = UnionFind(max_val + 1)
    for num in nums:
        for f in range(2, int(math.isqrt(num)) + 1):
            if num % f == 0:
                uf.union(num, f)
                uf.union(num, num // f)
    for i in range(len(nums)):
        if uf.find(nums[i]) != uf.find(sorted_nums[i]):
            return False
    return True