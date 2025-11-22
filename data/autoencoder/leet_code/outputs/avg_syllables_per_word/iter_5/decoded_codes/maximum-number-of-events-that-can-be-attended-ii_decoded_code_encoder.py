from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        events.sort(key=lambda x: x[1])
        n = len(events)
        ends = [e[1] for e in events]
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            j = bisect_right(ends, start - 1)
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]