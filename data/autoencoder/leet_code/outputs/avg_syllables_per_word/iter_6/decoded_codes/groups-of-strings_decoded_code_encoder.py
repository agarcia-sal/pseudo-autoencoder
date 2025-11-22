from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

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
                self.size[rootU] += self.size[rootV]
                self.rank[rootU] += 1

class Solution:
    def groupStrings(self, words):
        def bitmask(word):
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            return mask

        word_map = defaultdict(list)
        n = len(words)
        uf = UnionFind(n)

        masks = [bitmask(word) for word in words]
        for i, mask in enumerate(masks):
            word_map[mask].append(i)

        for i, mask in enumerate(masks):
            # Check masks that differ by one bit (toggle one letter)
            for j in range(26):
                new_mask = mask ^ (1 << j)
                if new_mask in word_map:
                    for k in word_map[new_mask]:
                        uf.union(i, k)

                # If the j-th bit is not set, try adding it
                if (mask & (1 << j)) == 0:
                    new_mask = mask | (1 << j)
                    if new_mask in word_map:
                        for k in word_map[new_mask]:
                            uf.union(i, k)

            # Check masks by replacing one letter with another (two bits changed)
            for j in range(26):
                if mask & (1 << j):
                    for k in range(26):
                        if (mask & (1 << k)) == 0:
                            new_mask = (mask ^ (1 << j)) | (1 << k)
                            if new_mask in word_map:
                                for l in word_map[new_mask]:
                                    uf.union(i, l)

        root_sizes = defaultdict(int)
        for i in range(n):
            root = uf.find(i)
            root_sizes[root] += 1

        max_group_size = max(root_sizes.values(), default=0)
        num_groups = len(root_sizes)

        return [num_groups, max_group_size]