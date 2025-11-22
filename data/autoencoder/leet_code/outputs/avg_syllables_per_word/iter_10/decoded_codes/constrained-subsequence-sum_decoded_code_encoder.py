from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]
        q = deque([0])

        for i in range(1, n):
            dp[i] = nums[i] + (dp[q[0]] if dp[q[0]] > 0 else 0)
            max_sum = max(max_sum, dp[i])

            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)

            if q[0] == i - k:
                q.popleft()

        return max_sum