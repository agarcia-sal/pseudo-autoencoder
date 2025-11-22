from collections import defaultdict

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
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
                self.size[rootU] += self.size[rootV]
                self.rank[rootU] += 1


class Solution:
    def groupStrings(self, words: list[str]) -> list[int]:
        def bitmask(word: str) -> int:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
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
                toggle_bit = 1 << j

                # 1) Toggle bit j
                new_mask = mask ^ toggle_bit
                if new_mask in word_map:
                    for k in word_map[new_mask]:
                        uf.union(i, k)

                # 2) If bit j is not set, try setting it
                if (mask & toggle_bit) == 0:
                    new_mask = mask | toggle_bit
                    if new_mask in word_map:
                        for k in word_map[new_mask]:
                            uf.union(i, k)

                # 3) If bit j is set, try swapping it with bit k that is not set
                if (mask & toggle_bit) != 0:
                    for k in range(26):
                        bit_k = 1 << k
                        if (mask & bit_k) == 0:
                            new_mask = (mask ^ toggle_bit) | bit_k
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