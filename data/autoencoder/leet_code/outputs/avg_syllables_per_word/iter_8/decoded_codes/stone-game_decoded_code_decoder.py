class Solution:
    def stoneGame(self, piles):
        def dfs(i, j):
            if i > j:
                return 0
            score_when_taking_i = piles[i] - dfs(i + 1, j)
            score_when_taking_j = piles[j] - dfs(i, j - 1)
            return max(score_when_taking_i, score_when_taking_j)
        return dfs(0, len(piles) - 1) > 0