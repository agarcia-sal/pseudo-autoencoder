class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        # is_palindrome[i][j] indicates if s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True

        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 2:
                    is_palindrome[start][end] = (s[start] == s[end])
                else:
                    is_palindrome[start][end] = (s[start] == s[end]) and is_palindrome[start + 1][end - 1]

        min_cuts = [0] * n
        for i in range(n):
            if is_palindrome[0][i]:
                min_cuts[i] = 0
            else:
                min_cuts[i] = float('inf')
                for j in range(1, i + 1):
                    if is_palindrome[j][i] and (min_cuts[j - 1] + 1 < min_cuts[i]):
                        min_cuts[i] = min_cuts[j - 1] + 1

        return min_cuts[-1]