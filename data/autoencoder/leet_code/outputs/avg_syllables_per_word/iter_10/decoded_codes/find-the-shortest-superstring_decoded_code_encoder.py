class Solution:
    def shortestSuperstring(self, words):
        n = len(words)

        overlap_cache = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    max_ov = min(len(words[i]), len(words[j]))
                    for k in range(max_ov, 0, -1):
                        if words[i][-k:] == words[j][:k]:
                            overlap_cache[i][j] = k
                            break

        from functools import lru_cache

        @lru_cache(None)
        def dp(mask, i):
            if mask == (1 << n) - 1:
                return 0, ""
            min_len = float('inf')
            best_path = ""
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    length, path = dp(mask | (1 << j), j)
                    length += len(words[j]) - overlap_cache[i][j]
                    if length < min_len:
                        min_len = length
                        best_path = words[j][overlap_cache[i][j]:] + path
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