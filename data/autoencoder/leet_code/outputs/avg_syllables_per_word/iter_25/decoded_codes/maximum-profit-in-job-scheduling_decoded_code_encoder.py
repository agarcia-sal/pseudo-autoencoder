from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Create a list of jobs as tuples (start, end, profit) and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        end_times = [job[1] for job in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Find the index j where jobs[i-1].start could be inserted in end_times to maintain sorted order
            j = bisect_right(end_times, jobs[i-1][0], hi=i-1)
            # Choose max between not taking this job or taking it plus best up to j
            dp[i] = max(dp[i-1], dp[j] + jobs[i-1][2])

        return dp[-1]