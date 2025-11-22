from collections import Counter
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique_nums = sorted(count.keys())
        dp = [0] * (len(unique_nums) + 1)
        dp[1] = unique_nums[0] * count[unique_nums[0]]

        for i in range(2, len(unique_nums) + 1):
            num = unique_nums[i - 1]
            if num == unique_nums[i - 2] + 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + num * count[num])
            else:
                dp[i] = dp[i - 1] + num * count[num]

        return dp[-1]