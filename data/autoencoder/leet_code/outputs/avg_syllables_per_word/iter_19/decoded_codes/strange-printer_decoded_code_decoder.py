class Solution:
    def strangePrinter(self, s):
        def dp(i, j, memo):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            # Print s[j] separately plus dp of s[i:j]
            result = dp(i, j - 1, memo) + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    # Combine printing s[k] and s[j] together
                    result = min(result, dp(i, k - 1, memo) + dp(k, j - 1, memo))
            memo[(i, j)] = result
            return result

        return dp(0, len(s) - 1, {})