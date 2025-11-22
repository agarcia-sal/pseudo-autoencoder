from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        increasing_subseq = []
        ans = []
        for obstacle in obstacles:
            idx = bisect_right(increasing_subseq, obstacle)
            if idx == len(increasing_subseq):
                increasing_subseq.append(obstacle)
            else:
                increasing_subseq[idx] = obstacle
            ans.append(idx + 1)
        return ans