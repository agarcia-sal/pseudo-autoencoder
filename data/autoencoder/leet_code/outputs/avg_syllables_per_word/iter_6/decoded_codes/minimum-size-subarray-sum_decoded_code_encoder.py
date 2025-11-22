class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, current_sum, min_length = 0, 0, float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0