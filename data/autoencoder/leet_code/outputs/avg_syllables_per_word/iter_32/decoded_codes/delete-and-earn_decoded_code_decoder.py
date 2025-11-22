from collections import Counter
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = Counter(nums)
        unique_nums = sorted(count.keys())
        n = len(unique_nums)

        dp = [0] * (n + 1)
        # Base case
        dp[1] = unique_nums[0] * count[unique_nums[0]]

        for i in range(2, n + 1):
            num = unique_nums[i - 1]
            prev_num = unique_nums[i - 2]
            if num == prev_num + 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + num * count[num])
            else:
                dp[i] = dp[i - 1] + num * count[num]

        return dp[-1]