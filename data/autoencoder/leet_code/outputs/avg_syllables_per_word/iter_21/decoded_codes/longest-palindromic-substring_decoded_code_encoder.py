class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        # Initialize a 2D list where f[i][j] indicates if s[i:j+1] is a palindrome
        f = [[True] * n for _ in range(n)]
        k = 0
        mx = 1
        # Fill the table bottom-up
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = False
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1]
                    if f[i][j] and (mx < j - i + 1):
                        k = i
                        mx = j - i + 1
        return s[k:k + mx]