from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp_list = [0] * (target + 1)
        dp_list[0] = 1
        for amount in range(1, target + 1):
            for number in nums:
                if amount >= number:
                    dp_list[amount] += dp_list[amount - number]
        return dp_list[target]