from typing import Dict, Tuple

class Solution:
    def strangePrinter(self, s: str) -> int:
        def dp(i: int, j: int, memo: Dict[Tuple[int, int], int]) -> int:
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            result = dp(i, j - 1, memo) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    candidate = dp(i, k, memo) + dp(k + 1, j - 1, memo)
                    if candidate < result:
                        result = candidate
            memo[(i, j)] = result
            return result

        return dp(0, len(s) - 1, {})