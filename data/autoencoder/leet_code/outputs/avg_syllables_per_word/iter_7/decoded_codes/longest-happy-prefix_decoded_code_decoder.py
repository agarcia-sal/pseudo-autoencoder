from typing import List

class Solution:
    def longestPrefix(self, s: str) -> str:
        n: int = len(s)
        lps: List[int] = [0] * n
        j: int = 0

        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j

        longest_happy_prefix_length: int = lps[-1]
        return s[:longest_happy_prefix_length]