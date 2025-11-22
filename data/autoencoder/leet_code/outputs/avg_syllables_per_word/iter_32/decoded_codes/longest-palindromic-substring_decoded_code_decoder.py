from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        # Initialize DP table f with True on the diagonals:
        # f[i][j] indicates whether s[i..j] is a palindrome
        f: List[List[bool]] = [[True]*n for _ in range(n)]
        k = 0  # start index of longest palindrome found
        mx = 1  # length of longest palindrome found

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = False
                if s[i] == s[j]:
                    # If the substring s[i+1..j-1] is palindrome or the substring length is 2 (then i+1>j-1)
                    if j - i == 1 or f[i + 1][j - 1]:
                        f[i][j] = True
                        length = j - i + 1
                        if length > mx:
                            k = i
                            mx = length

        return s[k:k + mx]