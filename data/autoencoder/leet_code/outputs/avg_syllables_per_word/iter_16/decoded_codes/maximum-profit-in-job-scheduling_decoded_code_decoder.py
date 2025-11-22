from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(((startTime[i], endTime[i], profit[i]) for i in range(len(startTime))), key=lambda x: x[1])
        end_times = [job[1] for job in jobs]
        dp = [0] * (len(jobs) + 1)
        for i in range(1, len(jobs) + 1):
            j = bisect_right(end_times, jobs[i - 1][0])
            dp[i] = max(dp[i - 1], dp[j] + jobs[i - 1][2])
        return dp[-1]