from math import inf
from typing import List, Tuple

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        def overlap(i: int, j: int) -> int:
            max_len = min(len(words[i]), len(words[j]))
            for k in range(max_len, 0, -1):
                if words[i][-k:] == words[j][:k]:
                    return k
            return 0

        from functools import lru_cache

        @lru_cache(None)
        def dp(mask: int, i: int) -> Tuple[int, str]:
            if mask == (1 << n) - 1:
                return 0, ''
            min_len = inf
            best_path = ''
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    length, path = dp(mask | (1 << j), j)
                    ol = overlap(i, j)
                    total_length = length + len(words[j]) - ol
                    if total_length < min_len:
                        min_len = total_length
                        # path portion excludes the overlapping prefix to avoid duplication
                        best_path = words[j][ol:] + path
            return min_len, best_path

        min_len = inf
        shortest_path = ''
        for i in range(n):
            length, path = dp(1 << i, i)
            total_length = length + len(words[i])
            if total_length < min_len:
                min_len = total_length
                shortest_path = words[i] + path

        return shortest_path