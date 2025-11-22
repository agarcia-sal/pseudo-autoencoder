class Solution:
    def shortestSuperstring(self, words):
        n = len(words)

        def overlap(i, j):
            max_olap = min(len(words[i]), len(words[j]))
            for k in range(max_olap, 0, -1):
                if words[i][-k:] == words[j][:k]:
                    return k
            return 0

        from functools import lru_cache

        @lru_cache(None)
        def dp(mask, i):
            if mask == (1 << n) - 1:
                return (0, "")
            min_len = float('inf')
            best_path = ""
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    length, path = dp(mask | (1 << j), j)
                    length += len(words[j]) - overlap(i, j)
                    if length < min_len:
                        min_len = length
                        olap = overlap(i, j)
                        best_path = words[j][olap:] + path
            return min_len, best_path

        min_len = float('inf')
        shortest_path = ""
        for i in range(n):
            length, path = dp(1 << i, i)
            length += len(words[i])
            if length < min_len:
                min_len = length
                shortest_path = words[i] + path

        return shortest_path