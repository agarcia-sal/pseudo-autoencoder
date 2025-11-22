from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the jobs into a list of tuples (start, end, profit)
        jobs = list(zip(startTime, endTime, profit))
        # Sort jobs by their end times
        jobs.sort(key=lambda x: x[1])
        # Extract end times for binary search
        end_times = [job[1] for job in jobs]
        n = len(jobs)
        # dp[i] represents max profit using first i jobs (1-indexed for convenience)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            current_start = jobs[i-1][0]
            # Find rightmost job that ends <= current_start
            j = bisect_right(end_times, current_start)
            # dp[i] = max of not taking current job or taking current job + best compatible
            dp[i] = max(dp[i-1], dp[j] + jobs[i-1][2])

        return dp[-1]