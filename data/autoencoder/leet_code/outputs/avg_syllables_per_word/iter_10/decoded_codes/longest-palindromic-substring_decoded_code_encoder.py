class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = [[True] * n for _ in range(n)]
        k, mx = 0, 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = False
                if s[i] == s[j]:
                    if j == i + 1 or f[i + 1][j - 1]:
                        f[i][j] = True
                        length = j - i + 1
                        if length > mx:
                            k, mx = i, length
        return s[k:k + mx]