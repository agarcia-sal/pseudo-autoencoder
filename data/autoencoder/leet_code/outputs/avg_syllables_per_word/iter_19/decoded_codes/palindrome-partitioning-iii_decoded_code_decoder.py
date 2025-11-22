import math

class Solution:
    def palindromePartition(self, s, k):
        def min_changes_to_palindrome(sub):
            i, j = 0, len(sub) - 1
            changes = 0
            while i < j:
                if sub[i] != sub[j]:
                    changes += 1
                i += 1
                j -= 1
            return changes

        n = len(s)
        dp = [[math.inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                for start in range(i):
                    changes = min_changes_to_palindrome(s[start:i])
                    if dp[start][j - 1] + changes < dp[i][j]:
                        dp[i][j] = dp[start][j - 1] + changes

        return dp[n][k]