from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        end_times = [job[1] for job in jobs]
        dp = [0] * (len(jobs) + 1)
        for i in range(1, len(jobs) + 1):
            j = bisect_right(end_times, jobs[i-1][0])  # Find the insertion point for start time
            dp[i] = max(dp[i-1], dp[j] + jobs[i-1][2])
        return dp[-1]