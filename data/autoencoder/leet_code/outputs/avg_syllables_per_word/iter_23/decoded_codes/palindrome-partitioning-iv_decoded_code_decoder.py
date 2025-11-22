class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        # Fill the is_pal table: is_pal[i][j] is True if s[i:j+1] is a palindrome
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        # Check for partitioning s into three palindromic substrings
        # s[0:i], s[i:j+1], s[j+1:n]
        for i in range(1, n - 1):
            if is_pal[0][i - 1]:
                for j in range(i, n - 1):
                    if is_pal[i][j] and is_pal[j + 1][n - 1]:
                        return True

        return False