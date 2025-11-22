class Solution:
    def searchRange(self, nums, target):
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = find_left(nums, target)
        right_index = find_right(nums, target)

        if 0 <= right_index < len(nums) and left_index <= right_index and nums[left_index] == target:
            return [left_index, right_index]
        return [-1, -1]