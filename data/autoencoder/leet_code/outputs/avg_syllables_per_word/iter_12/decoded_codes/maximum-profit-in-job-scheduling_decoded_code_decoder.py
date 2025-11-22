from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        end_times = [job[1] for job in jobs]
        dp = [0] * (len(jobs) + 1)

        for i in range(1, len(jobs) + 1):
            current_start = jobs[i - 1][0]
            j = bisect_right(end_times, current_start)
            profit_if_skip = dp[i - 1]
            profit_if_take = dp[j] + jobs[i - 1][2]
            dp[i] = max(profit_if_skip, profit_if_take)

        return dp[-1]