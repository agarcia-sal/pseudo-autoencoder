class Solution:
    def splitArray(self, nums, k):
        def canSplit(max_sum):
            current_sum = 0
            subarrays = 1
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num
            return subarrays <= k

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if canSplit(mid):
                right = mid
            else:
                left = mid + 1
        return left