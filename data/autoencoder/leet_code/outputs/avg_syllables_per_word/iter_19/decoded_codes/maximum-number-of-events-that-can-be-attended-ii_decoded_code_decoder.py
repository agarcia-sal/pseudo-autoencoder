from bisect import bisect_left

class Solution:
    def maxValue(self, events, k):
        # Sort events by their end time
        events.sort(key=lambda x: x[1])
        n = len(events)
        # dp[i][l]: max value by considering first i events choosing at most l events
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        ends = [event[1] for event in events]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the first event that ends before start (search for end >= start)
            j = bisect_left(ends, start)
            for l in range(1, k + 1):
                # Either skip current event or take it plus best until j
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]