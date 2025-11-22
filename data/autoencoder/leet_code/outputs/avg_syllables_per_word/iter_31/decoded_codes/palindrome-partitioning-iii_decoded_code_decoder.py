from math import inf

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def min_changes_to_palindrome(sub: str) -> int:
            i, j = 0, len(sub) - 1
            changes = 0
            while i < j:
                if sub[i] != sub[j]:
                    changes += 1
                i += 1
                j -= 1
            return changes

        n = len(s)
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            # j cannot be greater than both k and i (partitions cannot exceed substring length)
            for j in range(1, min(k, i) + 1):
                for start in range(i):
                    cost = min_changes_to_palindrome(s[start:i])
                    if dp[start][j - 1] != inf:
                        dp[i][j] = min(dp[i][j], dp[start][j - 1] + cost)

        return dp[n][k]