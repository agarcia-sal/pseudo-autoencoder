from math import inf

class Solution:
    def minimumFinishTime(self, tires, changeTime, numLaps):
        min_times = [inf] * 15
        for first_factor, reduction_factor in tires:
            total_time = 0
            for i in range(15):
                lap_time = first_factor * (reduction_factor ** i)
                if lap_time > changeTime + first_factor:
                    break
                total_time += lap_time
                if total_time < min_times[i]:
                    min_times[i] = total_time

        dp = [inf] * (numLaps + 1)
        dp[0] = 0
        for lap_count in range(1, numLaps + 1):
            for segment_length in range(min(lap_count, 15)):
                candidate_time = dp[lap_count - segment_length - 1] + min_times[segment_length] + changeTime
                if candidate_time < dp[lap_count]:
                    dp[lap_count] = candidate_time

        return dp[numLaps] - changeTime