from bisect import bisect_left

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        # Sort events by end day
        events.sort(key=lambda x: x[1])
        n = len(events)
        # dp[i][l]: max value using first i events with at most l events chosen
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        # Extract end days for binary search
        ends = [event[1] for event in events]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find earliest event j where end day >= start (binary search)
            j = bisect_left(ends, start)
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)
        return dp[n][k]