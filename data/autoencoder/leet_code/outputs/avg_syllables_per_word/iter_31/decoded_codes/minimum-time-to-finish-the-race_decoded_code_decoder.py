from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        min_times = [inf] * 15

        for first_value, rate in tires:
            total_time = 0
            for i in range(15):
                lap_time = first_value * (rate ** i)
                if lap_time > changeTime + first_value:
                    break
                total_time += lap_time
                if total_time < min_times[i]:
                    min_times[i] = total_time

        dp = [inf] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for j in range(min(i, 15)):
                candidate_time = dp[i - j - 1] + min_times[j] + changeTime
                if candidate_time < dp[i]:
                    dp[i] = candidate_time

        return dp[numLaps] - changeTime