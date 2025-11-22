from math import inf
from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        max_laps = 15
        min_times = [inf] * max_laps

        for f, r in tires:
            total_time = 0
            for i in range(max_laps):
                lap_time = f * (r ** i)
                if i > 0 and lap_time > changeTime + f:
                    break
                total_time += lap_time
                if total_time < min_times[i]:
                    min_times[i] = total_time

        dp = [inf] * (numLaps + 1)
        dp[0] = 0

        for i in range(1, numLaps + 1):
            limit = min(i, max_laps)
            for j in range(limit):
                time = dp[i - j - 1] + min_times[j] + changeTime
                if time < dp[i]:
                    dp[i] = time

        return dp[numLaps] - changeTime