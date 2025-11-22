from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        end_times = [job[1] for job in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            j = bisect_right(end_times, jobs[i - 1][0], 0, n)
            dp[i] = max(dp[i - 1], dp[j] + jobs[i - 1][2])
        return dp[-1]