from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def canFindAverage(mid: float) -> bool:
            prefix_sums = [0.0] * (len(nums) + 1)
            min_prefix_sum = [0.0] * (len(nums) + 1)
            for index in range(len(nums)):
                prefix_sums[index + 1] = prefix_sums[index] + nums[index] - mid
                if index >= k:
                    min_prefix_sum[index + 1] = min(min_prefix_sum[index], prefix_sums[index + 1 - k])
                else:
                    min_prefix_sum[index + 1] = min_prefix_sum[index]
                if index >= k - 1 and prefix_sums[index + 1] - min_prefix_sum[index + 1] >= 0:
                    return True
            return False

        low, high = min(nums), max(nums)
        precision = 1e-5
        while high - low > precision:
            mid = (low + high) / 2
            if canFindAverage(mid):
                low = mid
            else:
                high = mid
        return low