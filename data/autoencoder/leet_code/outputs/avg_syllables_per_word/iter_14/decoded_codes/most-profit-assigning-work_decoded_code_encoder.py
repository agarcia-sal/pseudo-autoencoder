from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        max_profit = 0
        best_profit = 0
        job_index = 0
        n = len(jobs)

        for ability in worker:
            while job_index < n and jobs[job_index][0] <= ability:
                best_profit = max(best_profit, jobs[job_index][1])
                job_index += 1
            max_profit += best_profit

        return max_profit