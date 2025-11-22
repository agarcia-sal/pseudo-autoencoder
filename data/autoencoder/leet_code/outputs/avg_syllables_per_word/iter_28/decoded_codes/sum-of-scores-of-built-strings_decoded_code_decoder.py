from typing import List

class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        lcp: List[int] = [0] * n
        l = 0
        r = 0
        for i in range(1, n):
            if i <= r:
                lcp[i] = min(r - i + 1, lcp[i - l])
            while i + lcp[i] < n and s[lcp[i]] == s[i + lcp[i]]:
                lcp[i] += 1
            if i + lcp[i] - 1 > r:
                l = i
                r = i + lcp[i] - 1
        return n + sum(lcp)