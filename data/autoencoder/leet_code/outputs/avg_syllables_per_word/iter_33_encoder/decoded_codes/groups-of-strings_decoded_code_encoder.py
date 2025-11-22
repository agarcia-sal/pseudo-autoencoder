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
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            return mask

        word_map = defaultdict(list)
        n = len(words)
        uf = UnionFind(n)

        for i, word in enumerate(words):
            mask = bitmask(word)
            word_map[mask].append(i)

        for i, word in enumerate(words):
            mask = bitmask(word)
            for j in range(26):
                bit = 1 << j
                # Toggle bit j
                new_mask = mask ^ bit
                if new_mask in word_map:
                    for k in word_map[new_mask]:
                        uf.union(i, k)

                # If bit j is not set, try setting it
                if (mask & bit) == 0:
                    new_mask = mask | bit
                    if new_mask in word_map:
                        for k in word_map[new_mask]:
                            uf.union(i, k)

                # If bit j is set, try swapping with an unset bit k
                if (mask & bit) != 0:
                    for k in range(26):
                        k_bit = 1 << k
                        if (mask & k_bit) == 0:
                            new_mask = (mask ^ bit) | k_bit
                            if new_mask in word_map:
                                for l in word_map[new_mask]:
                                    uf.union(i, l)

        root_sizes = defaultdict(int)
        for i in range(n):
            root = uf.find(i)
            root_sizes[root] += 1

        max_group_size = max(root_sizes.values()) if root_sizes else 0
        num_groups = len(root_sizes)

        return [num_groups, max_group_size]