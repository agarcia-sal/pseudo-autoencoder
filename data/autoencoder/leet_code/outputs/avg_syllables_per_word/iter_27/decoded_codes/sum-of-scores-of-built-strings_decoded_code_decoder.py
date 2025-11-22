from typing import List

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        lcp = [0] * n
        left_pointer = 0
        right_pointer = 0

        for i in range(1, n):
            if i <= right_pointer:
                lcp[i] = min(right_pointer - i + 1, lcp[i - left_pointer])
            while i + lcp[i] < n and s[lcp[i]] == s[i + lcp[i]]:
                lcp[i] += 1
            if i + lcp[i] - 1 > right_pointer:
                left_pointer = i
                right_pointer = i + lcp[i] - 1

        return sum(lcp) + n