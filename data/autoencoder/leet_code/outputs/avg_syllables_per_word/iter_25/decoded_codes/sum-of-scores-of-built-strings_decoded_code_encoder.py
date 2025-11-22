class Solution:
    def sumScores(self, s: str) -> int:
        n = len(s)
        lcp = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                lcp[i] = min(r - i + 1, lcp[i - l])
            while i + lcp[i] < n and s[lcp[i]] == s[i + lcp[i]]:
                lcp[i] += 1
            if i + lcp[i] - 1 > r:
                l, r = i, i + lcp[i] - 1
        total_score = sum(lcp) + n
        return total_score