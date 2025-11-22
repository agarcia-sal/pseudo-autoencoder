from bisect import bisect_left

class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        # Sort events by their end day
        events.sort(key=lambda x: x[1])
        n = len(events)
        # Extract end days for binary search keys
        ends = [event[1] for event in events]

        # Initialize dp array with zeros: (n+1) x (k+1)
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            # Find the position j where event with end day < start
            j = bisect_left(ends, start)
            for l in range(1, k + 1):
                # Max of not taking current event or taking current with previous compatible events
                dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + value)

        return dp[n][k]