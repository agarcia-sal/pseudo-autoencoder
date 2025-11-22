class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        def count(max_value):
            count = 0
            current_length = 0
            for num in nums:
                if num <= max_value:
                    current_length += 1
                    count += current_length
                else:
                    current_length = 0
            return count

        return count(right) - count(left - 1)