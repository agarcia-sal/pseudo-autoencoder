from bisect import bisect_right
from typing import List, Tuple

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.create_jobs_list(startTime, endTime, profit)
        self.sort_jobs_by_end_time()
        self.extract_end_times()
        self.initialize_dp_array(len(self.jobs) + 1)
        for index in range(1, len(self.jobs) + 1):
            j = self.find_latest_non_conflicting_job_index(self.end_times, self.jobs[index - 1][0])
            self.calculate_maximum_profit(index, j, self.dp, self.jobs)
        return self.dp[-1]

    def create_jobs_list(self, startTime: List[int], endTime: List[int], profit: List[int]) -> None:
        self.jobs: List[Tuple[int, int, int]] = list(zip(startTime, endTime, profit))

    def sort_jobs_by_end_time(self) -> None:
        self.jobs.sort(key=lambda job: job[1])

    def extract_end_times(self) -> None:
        self.end_times: List[int] = [job[1] for job in self.jobs]

    def initialize_dp_array(self, size: int) -> None:
        self.dp: List[int] = [0] * size

    def find_latest_non_conflicting_job_index(self, end_times: List[int], current_job_start: int) -> int:
        # bisect_right returns insertion position, so subtract 1 to get index of last job that ends <= current_job_start
        result = bisect_right(end_times, current_job_start)
        return result

    def calculate_maximum_profit(self, index: int, j: int, dp: List[int], jobs: List[Tuple[int,int,int]]) -> None:
        profit_if_taken = dp[j] + jobs[index - 1][2]
        profit_if_skipped = dp[index - 1]
        dp[index] = max(profit_if_taken, profit_if_skipped)