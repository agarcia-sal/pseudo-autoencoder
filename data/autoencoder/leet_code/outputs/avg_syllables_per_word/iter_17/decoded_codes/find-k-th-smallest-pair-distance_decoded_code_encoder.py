class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)

        def count(mid):
            pair_count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                pair_count += right - left
            return pair_count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left