from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        # min_times[i]: minimal total time to run i+1 continuous laps using same tire before needing a change
        min_times = [inf] * 15  # 0 to 14 index represents laps from 1 to 15
        for f, r in tires:
            total_time = 0
            for i in range(15):
                lap_time = f * (r ** i)
                # If it's better to change tire after previous lap than continue this lap, break
                if lap_time > changeTime + f:
                    break
                total_time += lap_time
                if total_time < min_times[i]:
                    min_times[i] = total_time

        dp = [inf] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            max_j = min(i - 1, 14)
            for j in range(max_j + 1):
                candidate_time = dp[i - j - 1] + min_times[j] + changeTime
                if candidate_time < dp[i]:
                    dp[i] = candidate_time

        return dp[numLaps] - changeTime