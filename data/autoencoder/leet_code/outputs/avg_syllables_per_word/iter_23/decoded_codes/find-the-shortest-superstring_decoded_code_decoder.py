from math import inf
from functools import lru_cache

class Solution:
    def shortestSuperstring(self, words):
        n = len(words)

        def overlap(i, j):
            # Find max k where suffix of words[i] equals prefix of words[j]
            max_len = min(len(words[i]), len(words[j]))
            for k in range(max_len, 0, -1):
                if words[i][-k:] == words[j][:k]:
                    return k
            return 0

        @lru_cache(maxsize=None)
        def dp(mask, i):
            if mask == (1 << n) - 1:
                return 0, ''
            min_len = inf
            best_path = ''
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    length, path = dp(mask | (1 << j), j)
                    overlap_len = overlap(i, j)
                    length += len(words[j]) - overlap_len
                    if length < min_len:
                        min_len = length
                        best_path = words[j][overlap_len:] + path
            return min_len, best_path

        min_len = inf
        shortest_path = ''
        for i in range(n):
            length, path = dp(1 << i, i)
            length += len(words[i])
            if length < min_len:
                min_len = length
                shortest_path = words[i] + path

        return shortest_path