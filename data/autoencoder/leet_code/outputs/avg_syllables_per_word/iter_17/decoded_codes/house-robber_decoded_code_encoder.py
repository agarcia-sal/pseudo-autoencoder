from typing import List

class Solution:
    def rob(self, list_of_numbers: List[int]) -> int:
        if not list_of_numbers:
            return 0
        if len(list_of_numbers) == 1:
            return list_of_numbers[0]

        dp = [0] * len(list_of_numbers)
        dp[0] = list_of_numbers[0]
        dp[1] = max(list_of_numbers[0], list_of_numbers[1])

        for i in range(2, len(list_of_numbers)):
            dp[i] = max(dp[i - 1], dp[i - 2] + list_of_numbers[i])

        return dp[-1]