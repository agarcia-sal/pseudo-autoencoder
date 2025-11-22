import math

def min_tire_change_time(tires, changeTime, numLaps):
    inf = math.inf
    min_times = [inf] * 15

    for f, r in tires:
        total = 0
        for i in range(15):
            lap = f * (r ** i)
            if lap > changeTime + f:
                break
            total += lap
            min_times[i] = min(min_times[i], total)

    dp = [inf] * (numLaps + 1)
    dp[0] = 0

    for i in range(1, numLaps + 1):
        for j in range(min(i, 15)):
            dp[i] = min(dp[i], dp[i - j - 1] + min_times[j] + changeTime)

    return dp[numLaps] - changeTime