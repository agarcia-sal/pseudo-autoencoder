class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        # Fill is_pal table to mark palindromic substrings
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        # Check for possible partitioning into three palindromic substrings
        for i in range(1, n - 1):
            if is_pal[0][i - 1]:
                for j in range(i, n - 1):
                    if is_pal[i][j] and is_pal[j + 1][n - 1]:
                        return True

        return False