import bisect
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Create a list of jobs as tuples (start, end, profit)
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        # Extract sorted end times
        end_times = [job[1] for job in jobs]
        # dp[i] will hold the max profit up to the i-th job (1-based indexing for convenience)
        dp = [0] * (len(jobs) + 1)

        for i in range(1, len(jobs) + 1):
            # Binary search for the last job that ends before the current job's start time
            # Use bisect_right to find insertion point for jobs[i-1][0] in end_times
            j = bisect.bisect_right(end_times, jobs[i - 1][0])  # jobs[i-1][0] is start time
            # dp[i] is max of skipping current job, or taking current job + dp[j]
            dp[i] = max(dp[i - 1], dp[j] + jobs[i - 1][2])
        return dp[-1]