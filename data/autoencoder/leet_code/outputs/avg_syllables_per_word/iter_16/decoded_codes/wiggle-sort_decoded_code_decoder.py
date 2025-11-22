class Solution:
    def wiggleSort(self, nums) -> None:
        less = True
        for i in range(len(nums) - 1):
            if less:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            less = not less