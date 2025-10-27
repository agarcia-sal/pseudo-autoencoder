class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        sorted_nums = nums[:]
        n = len(nums)
        left = (n - 1) // 2
        right = n - 1
        for index in range(n):
            if index % 2 == 0:
                nums[index] = sorted_nums[left]
                left -= 1
            else:
                nums[index] = sorted_nums[right]
                right -= 1