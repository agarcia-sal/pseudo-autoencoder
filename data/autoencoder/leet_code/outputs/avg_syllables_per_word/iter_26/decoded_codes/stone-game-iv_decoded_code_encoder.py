class Solution:
    def winnerSquareGame(self, number_of_stones: int) -> bool:
        dp = [False] * (number_of_stones + 1)
        for i in range(1, number_of_stones + 1):
            square_root_candidate = 1
            while square_root_candidate * square_root_candidate <= i:
                if not dp[i - square_root_candidate * square_root_candidate]:
                    dp[i] = True
                    break
                square_root_candidate += 1
        return dp[number_of_stones]