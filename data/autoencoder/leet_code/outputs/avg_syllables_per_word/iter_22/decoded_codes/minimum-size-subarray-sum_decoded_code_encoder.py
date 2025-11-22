class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                length = right - left + 1
                if length < min_length:
                    min_length = length
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0