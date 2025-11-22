from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        min_times = [inf] * 15
        for fixed_time, rate in tires:
            total_time = 0
            for i in range(15):
                lap_time = fixed_time * (rate ** i)
                if lap_time > changeTime + fixed_time:
                    break
                total_time += lap_time
                if total_time < min_times[i]:
                    min_times[i] = total_time

        dp = [inf] * (numLaps + 1)
        dp[0] = 0
        for i in range(1, numLaps + 1):
            for j in range(min(i, 15)):
                current_value = dp[i - j - 1] + min_times[j] + changeTime
                if current_value < dp[i]:
                    dp[i] = current_value

        return dp[numLaps] - changeTime