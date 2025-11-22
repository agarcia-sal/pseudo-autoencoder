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
        dp = self.dp_initialization(n, k)

        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                for start in range(i):
                    changes = min_changes_to_palindrome(s[start:i])
                    current = dp[start][j - 1] + changes
                    if dp[i][j] > current:
                        dp[i][j] = current

        return dp[n][k]

    def dp_initialization(self, n: int, k: int) -> list:
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        return dp