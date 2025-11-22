import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        n = len(obstacles)
        ans = []
        increasing_subseq = []

        for obstacle in obstacles:
            # Find the insertion position to maintain non-decreasing order
            # using bisect_right to ensure "LESS THAN OR EQUAL TO" for elements before idx
            idx = bisect.bisect_right(increasing_subseq, obstacle)

            if idx == len(increasing_subseq):
                increasing_subseq.append(obstacle)
            else:
                increasing_subseq[idx] = obstacle

            ans.append(idx + 1)

        return ans