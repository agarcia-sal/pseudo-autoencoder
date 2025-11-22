from bisect import bisect_left

def max_value(events, k):
    # Sort events by end day
    events.sort(key=lambda x: x[1])
    n = len(events)

    # Extract end days for binary search
    end_days = [e[1] for e in events]

    # Initialize dp array
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        s, e, v = events[i - 1]
        # Find the rightmost event that ends before event[i-1] starts (s)
        j = bisect_left(end_days, s)  # all events ending before s are at indices < j

        for l in range(1, k + 1):
            dp[i][l] = max(dp[i - 1][l], dp[j][l - 1] + v)

    return dp[n][k]