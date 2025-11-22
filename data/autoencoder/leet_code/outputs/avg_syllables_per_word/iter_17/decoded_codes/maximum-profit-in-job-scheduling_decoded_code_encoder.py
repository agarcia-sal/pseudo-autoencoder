from bisect import bisect_right
from typing import List, Tuple

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = self.SortJobsByEndTime(startTime, endTime, profit)
        end_times = self.ExtractEndTimes(jobs)
        dp = self.InitializeDPArray(len(jobs) + 1)
        for index in range(1, len(jobs) + 1):
            current_job_start = jobs[index - 1][0]
            j = self.FindPositionRight(end_times, current_job_start)
            dp[index] = max(dp[index - 1], dp[j] + jobs[index - 1][2])
        return dp[-1]

    def SortJobsByEndTime(self, startTime: List[int], endTime: List[int], profit: List[int]) -> List[Tuple[int, int, int]]:
        # Sort the jobs by endTime with tuples (startTime, endTime, profit)
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda job: job[1])
        return jobs

    def ExtractEndTimes(self, jobs: List[Tuple[int, int, int]]) -> List[int]:
        # Extract the end times from sorted jobs
        return [job[1] for job in jobs]

    def InitializeDPArray(self, length: int) -> List[int]:
        # Initialize DP array with zeros
        return [0] * length

    def FindPositionRight(self, sorted_list: List[int], value: int) -> int:
        # Binary search for insertion point to the right of value
        # bisect_right returns an insertion index in sorted_list to keep order
        return bisect_right(sorted_list, value)