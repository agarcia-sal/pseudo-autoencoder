class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        INF = float('inf')
        max_consecutive = 15
        min_times = [INF] * max_consecutive

        for f, r in tires:
            total_time = 0
            for i in range(max_consecutive):
                lap_time = f * (r ** i)
                if i > 0 and lap_time > changeTime + f:
                    break
                total_time += lap_time
                if total_time < min_times[i]:
                    min_times[i] = total_time

        dp = [INF] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for j in range(min(i, max_consecutive)):
                dp[i] = min(dp[i], dp[i - j - 1] + min_times[j] + changeTime)

        return dp[numLaps] - changeTime