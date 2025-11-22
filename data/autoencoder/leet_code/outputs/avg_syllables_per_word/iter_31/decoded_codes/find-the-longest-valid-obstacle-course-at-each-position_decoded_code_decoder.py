from bisect import bisect_right
from typing import List

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = []
        increasing_subseq = []

        for obstacle in obstacles:
            # Find the insertion position to the right to maintain non-decreasing order
            idx = bisect_right(increasing_subseq, obstacle)
            if idx == len(increasing_subseq):
                increasing_subseq.append(obstacle)
            else:
                increasing_subseq[idx] = obstacle
            ans.append(idx + 1)

        return ans