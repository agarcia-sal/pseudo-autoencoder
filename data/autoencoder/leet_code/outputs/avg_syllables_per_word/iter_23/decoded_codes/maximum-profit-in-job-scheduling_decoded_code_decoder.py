from bisect import bisect_left
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the input lists into a list of tuples and sort by endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        end_times = [job[1] for job in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            curr_start = jobs[i-1][0]
            curr_profit = jobs[i-1][2]

            # Binary search for rightmost job that ends <= current start time
            # bisect_left gives insertion position. We use curr_start to find jobs that end <= curr_start 
            j = bisect_left(end_times, curr_start)
            # check equality condition, but do nothing if equal as per pseudocode (i.e. no special action)
            # so skip that condition as it results in no code change

            dp[i] = max(dp[i-1], dp[j] + curr_profit)

        return dp[-1]