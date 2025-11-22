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
                    temp_result = dp(i, k - 1, memo) + dp(k, j - 1, memo)
                    if temp_result < result:
                        result = temp_result
            memo[(i, j)] = result
            return result
        return dp(0, len(s) - 1, {})