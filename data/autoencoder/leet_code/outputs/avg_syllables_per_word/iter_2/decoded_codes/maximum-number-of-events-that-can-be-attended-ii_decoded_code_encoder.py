from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        # Sort events by their end day
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Extract the end days for binary search
        end_days = [event[1] for event in events]

        # Initialize dp array with 0's
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the rightmost event that ends before 'start'
            j = bisect_right(end_days, start - 1)

            for l in range(1, k + 1):
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]