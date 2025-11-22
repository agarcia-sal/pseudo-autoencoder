from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        min_times = [inf] * 15

        for first_factor, reduction_factor in tires:
            total_time = 0
            for index in range(15):
                lap_time = first_factor * (reduction_factor ** index)
                if lap_time > changeTime + first_factor:
                    break
                total_time += lap_time
                if total_time < min_times[index]:
                    min_times[index] = total_time

        dp = [inf] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for j in range(min(i, 15)):
                candidate = dp[i - j - 1] + min_times[j] + changeTime
                if candidate < dp[i]:
                    dp[i] = candidate

        return dp[numLaps] - changeTime