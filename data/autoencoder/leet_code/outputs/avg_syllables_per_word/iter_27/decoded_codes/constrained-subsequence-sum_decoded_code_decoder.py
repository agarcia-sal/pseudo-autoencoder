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
            dp_at_q_front = dp[q[0]] if dp[q[0]] > 0 else 0
            dp[i] = nums[i] + dp_at_q_front

            if dp[i] > max_sum:
                max_sum = dp[i]

            while q and dp[i] >= dp[q[-1]]:
                q.pop()

            q.append(i)

            if q[0] == i - k:
                q.popleft()

        return max_sum