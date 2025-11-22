class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left_pointer = 0
        current_sum = 0
        minimum_length = float('inf')

        for right_pointer in range(len(nums)):
            current_sum += nums[right_pointer]
            while current_sum >= target:
                minimum_length = min(minimum_length, right_pointer - left_pointer + 1)
                current_sum -= nums[left_pointer]
                left_pointer += 1

        return minimum_length if minimum_length != float('inf') else 0