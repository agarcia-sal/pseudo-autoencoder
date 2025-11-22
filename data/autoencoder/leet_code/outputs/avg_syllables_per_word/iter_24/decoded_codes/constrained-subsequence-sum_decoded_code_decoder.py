from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]
        q = deque([0])
        for i in range(1, n):
            if q and q[0] >= 0 and dp[q[0]] > 0:
                value = dp[q[0]]
            else:
                value = 0
            dp[i] = nums[i] + value
            if dp[i] > max_sum:
                max_sum = dp[i]
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
        return max_sum