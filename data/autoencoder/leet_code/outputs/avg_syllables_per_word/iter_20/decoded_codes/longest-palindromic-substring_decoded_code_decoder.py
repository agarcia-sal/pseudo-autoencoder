class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # f[i][j] will be True if s[i..j] is a palindrome
        f = [[True] * n for _ in range(n)]
        k = 0
        mx = 1

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = False
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] if j - i > 1 else True
                    if f[i][j] and mx < (j - i + 1):
                        k = i
                        mx = j - i + 1

        return s[k:k + mx]