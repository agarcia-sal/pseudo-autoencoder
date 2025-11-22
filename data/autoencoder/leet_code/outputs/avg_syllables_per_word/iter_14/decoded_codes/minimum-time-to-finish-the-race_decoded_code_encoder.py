from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime: int, numLaps: int) -> int:
        min_times = [inf] * 15

        for tire in tires:
            f, r = tire
            total_time = 0
            for i in range(15):
                lap_time = f * (r ** i)
                if lap_time > changeTime + f:
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