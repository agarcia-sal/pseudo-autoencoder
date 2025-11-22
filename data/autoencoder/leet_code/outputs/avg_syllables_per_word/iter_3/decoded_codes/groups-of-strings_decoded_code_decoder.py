from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v):
        rootU, rootV = self.find(u), self.find(v)
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

        masks = []
        for i, word in enumerate(words):
            m = bitmask(word)
            masks.append(m)
            word_map[m].append(i)

        for i in range(n):
            mask = masks[i]
            for j in range(26):
                toggle = 1 << j
                new_mask = mask ^ toggle  # Delete or replace letter
                if new_mask in word_map:
                    for k in word_map[new_mask]:
                        uf.union(i, k)

                if (mask & toggle) == 0:  # Add letter
                    new_mask = mask | toggle
                    if new_mask in word_map:
                        for k in word_map[new_mask]:
                            uf.union(i, k)

                if (mask & toggle) != 0:  # Replace letter
                    for k in range(26):
                        add = 1 << k
                        if (mask & add) == 0:
                            replaced_mask = (mask ^ toggle) | add
                            if replaced_mask in word_map:
                                for l in word_map[replaced_mask]:
                                    uf.union(i, l)

        root_sizes = defaultdict(int)
        for i in range(n):
            root_sizes[uf.find(i)] += 1

        max_group_size = max(root_sizes.values()) if root_sizes else 0
        num_groups = len(root_sizes)

        return [num_groups, max_group_size]