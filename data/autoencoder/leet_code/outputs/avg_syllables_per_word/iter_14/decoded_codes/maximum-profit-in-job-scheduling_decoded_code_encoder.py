import bisect
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the job attributes and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        # Extract sorted end times for binary searching
        end_times = [job[1] for job in jobs]

        n = len(jobs)
        dp = [0] * (n + 1)  # dp[i] = max profit for first i jobs

        for i in range(1, n + 1):
            start_i, end_i, profit_i = jobs[i - 1]
            # Find the rightmost job with end time <= current start time
            j = bisect.bisect_right(end_times, start_i) - 1
            if j < 0:
                j = 0
            dp[i] = max(dp[i - 1], dp[j + 1] + profit_i if j >= 0 else profit_i)

        return dp[-1]