from typing import List

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        number_of_piles = len(piles)
        dp = self.initialize_dp_table(number_of_piles, k)

        for index_pile in range(1, number_of_piles + 1):
            current_pile = self.get_current_pile(piles, index_pile)
            for coins_chosen in range(1, k + 1):
                accumulated_value = 0
                maximum_coins_to_take = min(coins_chosen, len(current_pile))
                for coins_taken in range(maximum_coins_to_take + 1):
                    if coins_taken > 0:
                        accumulated_value += current_pile[coins_taken - 1]
                    candidate_value = dp[index_pile - 1][coins_chosen - coins_taken] + accumulated_value
                    dp[index_pile][coins_chosen] = max(dp[index_pile][coins_chosen], candidate_value)

        return dp[number_of_piles][k]

    def initialize_dp_table(self, number_of_piles: int, maximum_coins: int) -> List[List[int]]:
        return [[0] * (maximum_coins + 1) for _ in range(number_of_piles + 1)]

    def get_current_pile(self, piles: List[List[int]], index_pile: int) -> List[int]:
        return piles[index_pile - 1]