class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = self.initializeTwoDimensionalList(n, n, True)
        k = 0
        mx = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = False
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1]
                    if f[i][j] and mx < j - i + 1:
                        k = i
                        mx = j - i + 1
        return s[k:k + mx]

    def initializeTwoDimensionalList(self, rows: int, columns: int, value) -> list:
        result = []
        for _ in range(rows):
            current_row = []
            for _ in range(columns):
                current_row.append(value)
            result.append(current_row)
        return result