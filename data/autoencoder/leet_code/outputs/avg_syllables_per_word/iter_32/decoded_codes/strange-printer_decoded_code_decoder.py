from typing import Dict, Tuple

class Solution:
    def strangePrinter(self, s: str) -> int:
        def dp(i: int, j: int, memo: Dict[Tuple[int, int], int]) -> int:
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            # Initialize result as printing s[i:j] by printing s[i:j-1] plus one more print
            result = dp(i, j - 1, memo) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    # Minimize the prints by merging same chars at s[k] and s[j]
                    result = min(result, dp(i, k, memo) + dp(k + 1, j - 1, memo))
            memo[(i, j)] = result
            return result

        return dp(0, len(s) - 1, {})