from typing import List

class Solution:
    def canPartition(self, list_of_numbers: List[int]) -> bool:
        total_sum = sum(list_of_numbers)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(list_of_numbers)

        dp = [False] * (target + 1)
        dp[0] = True

        for num in list_of_numbers:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]