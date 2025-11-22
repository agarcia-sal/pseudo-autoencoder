from typing import List

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def longest_palindromic_subseq(s: str) -> int:
            n = len(s)
            dp: List[List[int]] = [[0] * n for _ in range(n)]
            for i in range(n):
                dp[i][i] = 1
            for length in range(2, n + 1):
                for i in range(n - length + 1):
                    j = i + length - 1
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            return dp[0][n - 1] if n > 0 else 0

        longest_palindrome_length = longest_palindromic_subseq(s)
        return len(s) - longest_palindrome_length <= k