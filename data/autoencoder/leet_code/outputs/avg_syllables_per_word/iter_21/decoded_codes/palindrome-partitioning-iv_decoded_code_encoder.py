class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        def initialize_palindrome_matrix(size: int):
            return [[False] * size for _ in range(size)]

        is_pal = initialize_palindrome_matrix(n)

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        for i in range(1, n - 1):
            if is_pal[0][i - 1]:
                for j in range(i, n - 1):
                    if is_pal[i][j] and is_pal[j + 1][n - 1]:
                        return True

        return False