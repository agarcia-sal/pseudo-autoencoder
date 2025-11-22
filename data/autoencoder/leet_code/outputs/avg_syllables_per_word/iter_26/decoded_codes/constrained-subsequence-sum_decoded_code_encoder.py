from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]

        reference = deque([0])
        for i in range(1, n):
            dp[i] = nums[i] + (dp[reference[0]] if dp[reference[0]] > 0 else 0)
            if dp[i] > max_sum:
                max_sum = dp[i]

            while reference and dp[i] >= dp[reference[-1]]:
                reference.pop()
            reference.append(i)

            if reference[0] == i - k:
                reference.popleft()

        return max_sum