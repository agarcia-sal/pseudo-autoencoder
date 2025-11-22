from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]
        pointer = deque([0])

        for i in range(1, n):
            dp_element = dp[pointer[0]] if dp[pointer[0]] > 0 else 0
            dp[i] = nums[i] + dp_element
            if dp[i] > max_sum:
                max_sum = dp[i]

            while pointer and dp[i] >= dp[pointer[-1]]:
                pointer.pop()

            pointer.append(i)

            if pointer[0] == i - k:
                pointer.popleft()

        return max_sum