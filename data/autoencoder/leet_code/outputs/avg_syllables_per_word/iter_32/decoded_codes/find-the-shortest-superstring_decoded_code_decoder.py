from functools import lru_cache
from math import inf
from typing import List, Tuple

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        def overlap(i: int, j: int) -> int:
            # Find max length k s.t. suffix of words[i] == prefix of words[j]
            max_olap = min(len(words[i]), len(words[j]))
            for k in range(max_olap, 0, -1):
                if words[i][-k:] == words[j][:k]:
                    return k
            return 0

        @lru_cache(None)
        def dp(mask: int, i: int) -> Tuple[int, str]:
            # If all words are included
            if mask == (1 << n) - 1:
                return 0, ""

            min_len = inf
            best_path = ""
            for j in range(n):
                if (mask & (1 << j)) == 0:
                    olap = overlap(i, j)
                    length, path = dp(mask | (1 << j), j)
                    length += len(words[j]) - olap
                    if length < min_len:
                        min_len = length
                        # Append non-overlapping suffix of words[j]
                        best_path = words[j][olap:] + path
            return min_len, best_path

        min_len = inf
        shortest_path = ""
        for i in range(n):
            length, path = dp(1 << i, i)
            length += len(words[i])
            if length < min_len:
                min_len = length
                shortest_path = words[i] + path

        return shortest_path