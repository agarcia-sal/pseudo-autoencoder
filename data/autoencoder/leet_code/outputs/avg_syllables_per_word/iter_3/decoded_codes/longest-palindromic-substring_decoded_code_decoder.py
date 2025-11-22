class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = [[True] * n for _ in range(n)]
        k = 0
        mx = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = False
                if s[i] == s[j]:
                    if j - i == 1 or f[i + 1][j - 1]:
                        f[i][j] = True
                        if mx < j - i + 1:
                            k = i
                            mx = j - i + 1
        return s[k:k + mx]