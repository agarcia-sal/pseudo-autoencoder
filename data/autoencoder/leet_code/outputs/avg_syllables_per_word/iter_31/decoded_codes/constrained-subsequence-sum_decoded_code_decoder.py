from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]

        q = deque([0])

        for i in range(1, n):
            # If the max dp in range is positive, add it to nums[i], else just nums[i]
            dp[i] = nums[i] + (dp[q[0]] if dp[q[0]] > 0 else 0)

            if dp[i] > max_sum:
                max_sum = dp[i]

            # Remove indices with dp values less than or equal to current dp[i] for max deque property
            while q and dp[i] >= dp[q[-1]]:
                q.pop()

            q.append(i)

            # Remove indices outside the window of size k
            if q[0] == i - k:
                q.popleft()

        return max_sum