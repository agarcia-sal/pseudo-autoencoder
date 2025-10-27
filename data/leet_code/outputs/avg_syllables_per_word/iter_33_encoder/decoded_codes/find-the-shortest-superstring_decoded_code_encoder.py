from math import inf
from functools import lru_cache

class Solution:
    def shortestSuperstring(self, words):
        n = len(words)

        def overlap(i, j):
            # Find max length k where suffix of words[i] matches prefix of words[j]
            max_overlap = min(len(words[i]), len(words[j]))
            for k in range(max_overlap, 0, -1):
                if words[i][-k:] == words[j][:k]:
                    return k
            return 0

        @lru_cache(None)
        def dp(mask, i):
            if mask == (1 << n) - 1:
                return 0, ''
            min_len = inf
            best_path = ''
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    length, path = dp(mask | (1 << j), j)
                    length += len(words[j]) - overlap(i, j)
                    if length < min_len:
                        min_len = length
                        o = overlap(i, j)
                        best_path = words[j][o:] + path
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