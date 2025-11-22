from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        # f[i][j] will be True if s[i..j] is a palindrome
        f: List[List[bool]] = [[True] * n for _ in range(n)]
        max_len = 1
        start = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = False
                if s[i] == s[j]:
                    if j - i == 1:
                        # Two equal chars side by side are palindrome
                        f[i][j] = True
                    else:
                        f[i][j] = f[i + 1][j - 1]
                    if f[i][j] and (j - i + 1) > max_len:
                        start = i
                        max_len = j - i + 1

        return s[start:start + max_len]