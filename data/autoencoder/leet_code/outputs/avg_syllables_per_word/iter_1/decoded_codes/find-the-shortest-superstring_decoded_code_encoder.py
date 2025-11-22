def shortest_superstring(words):
    n = len(words)

    def overlap(i, j):
        max_len = min(len(words[i]), len(words[j]))
        for k in range(max_len, 0, -1):
            if words[i][-k:] == words[j][:k]:
                return k
        return 0

    from functools import lru_cache

    @lru_cache(None)
    def dp(mask, i):
        if mask == (1 << n) - 1:
            return 0, ""
        min_len = float('inf')
        best_path = ""
        for j in range(n):
            if not (mask & (1 << j)):
                length, path = dp(mask | (1 << j), j)
                ov = overlap(i, j)
                length += len(words[j]) - ov
                if length < min_len:
                    min_len, best_path = length, words[j][ov:] + path
        return min_len, best_path

    min_len = float('inf')
    shortest_path = ""
    for i in range(n):
        length, path = dp(1 << i, i)
        length += len(words[i])
        if length < min_len:
            min_len, shortest_path = length, words[i] + path

    return shortest_path