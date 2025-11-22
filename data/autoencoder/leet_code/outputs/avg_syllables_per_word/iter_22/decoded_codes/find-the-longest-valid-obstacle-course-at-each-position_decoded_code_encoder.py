from bisect import bisect_right

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        n = len(obstacles)
        ans = []
        increasing_subseq = []

        for obstacle in obstacles:
            # find rightmost place to insert obstacle (i.e., first element > obstacle)
            idx = bisect_right(increasing_subseq, obstacle)
            if idx == len(increasing_subseq):
                increasing_subseq.append(obstacle)
            else:
                increasing_subseq[idx] = obstacle
            ans.append(idx + 1)

        return ans