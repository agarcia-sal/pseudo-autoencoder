class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1

        from math import inf

        def dp(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            min_difficulty = inf
            current_max = 0
            for j in range(i, n - d + 1):
                current_max = max(current_max, jobDifficulty[j])
                tentative_difficulty = current_max + dp(j + 1, d - 1)
                min_difficulty = min(min_difficulty, tentative_difficulty)
            return min_difficulty

        return dp(0, d)