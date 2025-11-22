import bisect

class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0

        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)