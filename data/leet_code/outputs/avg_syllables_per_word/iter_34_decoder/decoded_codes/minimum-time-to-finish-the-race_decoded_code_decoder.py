import math
from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        min_times = [math.inf] * 15  # min total time for up to 15 consecutive laps without changing tire

        for f, r in tires:
            total_time = 0
            for i in range(15):
                lap_time = f * (r ** i)
                if lap_time > changeTime + f:
                    break
                total_time += lap_time
                if total_time < min_times[i]:
                    min_times[i] = total_time

        dp = [math.inf] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            for j in range(min(i, 15)):
                candidate_time = dp[i - j - 1] + min_times[j] + changeTime
                if candidate_time < dp[i]:
                    dp[i] = candidate_time

        return dp[numLaps] - changeTime