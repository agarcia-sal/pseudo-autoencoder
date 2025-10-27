class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        def canFindAverage(mid: float) -> bool:
            n = len(nums)
            prefix_sums = [0.0] * (n + 1)
            min_prefix_sum = [0.0] * (n + 1)
            for i in range(n):
                prefix_sums[i + 1] = prefix_sums[i] + nums[i] - mid
                if i >= k:
                    min_prefix_sum[i + 1] = min(min_prefix_sum[i], prefix_sums[i + 1 - k])
                else:
                    min_prefix_sum[i + 1] = min_prefix_sum[i]
                if i >= k - 1 and prefix_sums[i + 1] - min_prefix_sum[i + 1] >= 0:
                    return True
            return False

        low, high = min(nums), max(nums)
        while high - low > 0.0001:
            mid = (low + high) / 2
            if canFindAverage(mid):
                low = mid
            else:
                high = mid
        return low