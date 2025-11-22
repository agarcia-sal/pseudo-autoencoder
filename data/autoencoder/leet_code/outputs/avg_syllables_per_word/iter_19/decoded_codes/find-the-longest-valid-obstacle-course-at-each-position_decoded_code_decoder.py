from bisect import bisect_right
from typing import List

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        increasing_subseq = []  # smallest tail values for non-decreasing subsequences by length

        for obstacle in obstacles:
            idx = bisect_right(increasing_subseq, obstacle)
            if idx == len(increasing_subseq):
                increasing_subseq.append(obstacle)
            else:
                increasing_subseq[idx] = obstacle
            ans.append(idx + 1)

        return ans