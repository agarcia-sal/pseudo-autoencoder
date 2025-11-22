class Solution:
    def strangePrinter(self, string_s: str) -> int:
        def dp(i: int, j: int, memo: dict) -> int:
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            result = dp(i, j - 1, memo) + 1
            for k in range(i, j):
                if string_s[k] == string_s[j]:
                    candidate = dp(i, k, memo) + dp(k + 1, j - 1, memo)
                    if candidate < result:
                        result = candidate
            memo[(i, j)] = result
            return result

        return dp(0, len(string_s) - 1, {})