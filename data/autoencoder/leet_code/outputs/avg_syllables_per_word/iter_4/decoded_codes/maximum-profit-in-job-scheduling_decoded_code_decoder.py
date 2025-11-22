from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        end_times = [job[1] for job in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            start_i = jobs[i-1][0]
            profit_i = jobs[i-1][2]
            j = bisect.bisect_right(end_times, start_i)
            dp[i] = max(dp[i-1], dp[j] + profit_i)

        return dp[-1]