from math import inf

class Solution:
    def shortestSuperstring(self, words):
        n = len(words)

        def overlap(i, j):
            max_len = min(len(words[i]), len(words[j]))
            for k in range(max_len, 0, -1):
                if words[i][-k:] == words[j][:k]:
                    return k
            return 0

        memo = {}

        def dp(mask, i):
            if mask == (1 << n) - 1:
                return 0, ""
            if (mask, i) in memo:
                return memo[(mask, i)]

            min_len = inf
            best_path = ""
            for j in range(n):
                if not (mask & (1 << j)):
                    length, path = dp(mask | (1 << j), j)
                    length += len(words[j]) - overlap(i, j)
                    if length < min_len:
                        min_len = length
                        ov = overlap(i, j)
                        best_path = words[j][ov:] + path
            memo[(mask, i)] = (min_len, best_path)
            return memo[(mask, i)]

        min_len = inf
        shortest_path = ""
        for i in range(n):
            length, path = dp(1 << i, i)
            length += len(words[i])
            if length < min_len:
                min_len = length
                shortest_path = words[i] + path
        return shortest_path