from bisect import bisect_left

class Solution:
    def maxValue(self, events, k):
        # Sort events by their end day
        events.sort(key=lambda e: e[1])
        n = len(events)

        # Extract end days separately for binary search
        end_days = [event[1] for event in events]

        # dp[i][j]: max value using first i events with j events chosen
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start_day, end_day, value = events[i - 1]
            # Find position j where end_day_j >= start_day by binary search
            # We want the largest index with end_day < start_day so dp can use dp[j][...]
            pos = bisect_left(end_days, start_day)
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[pos][l - 1] + value)

        return dp[n][k]