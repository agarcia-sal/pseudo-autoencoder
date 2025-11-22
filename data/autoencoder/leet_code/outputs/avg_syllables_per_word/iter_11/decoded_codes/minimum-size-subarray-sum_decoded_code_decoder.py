class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                if min_length > right - left + 1:
                    min_length = right - left + 1
                current_sum -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        else:
            return min_length