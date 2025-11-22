class Solution:
    def stoneGame(self, piles):
        def dfs(i, j):
            if i > j:
                return 0
            left_choice = piles[i] - dfs(i + 1, j)
            right_choice = piles[j] - dfs(i, j - 1)
            return max(left_choice, right_choice)

        initial_result = dfs(0, len(piles) - 1)
        return initial_result > 0