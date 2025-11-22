class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)

        def count(mid):
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        left = 0
        right = nums[n - 1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left