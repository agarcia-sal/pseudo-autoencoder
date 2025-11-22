from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        min_times = [inf] * 15

        for first_factor, rate in tires:
            total_time = 0
            for idx in range(15):
                lap_time = first_factor * (rate ** idx)
                if lap_time > changeTime + first_factor:
                    break
                total_time += lap_time
                if total_time < min_times[idx]:
                    min_times[idx] = total_time

        dp = [inf] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            upper_bound = min(i, 15)
            for j in range(upper_bound):
                candidate = dp[i - j - 1] + min_times[j] + changeTime
                if candidate < dp[i]:
                    dp[i] = candidate

        return dp[numLaps] - changeTime