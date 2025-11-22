from bisect import bisect_left

class Solution:
    def maxValue(self, events, k):
        # Sort events by their end day
        events.sort(key=lambda x: x[1])
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Extract the end days for binary search
        end_days = [e[1] for e in events]

        for i in range(1, n + 1):
            start_day, end_day, event_value = events[i - 1]
            # Find the leftmost position where the end day is >= start_day
            j = bisect_left(end_days, start_day)
            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + event_value)

        return dp[n][k]