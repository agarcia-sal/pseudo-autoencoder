from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            # If duplicates at left, mid, and right, move pointers inward to skip duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False