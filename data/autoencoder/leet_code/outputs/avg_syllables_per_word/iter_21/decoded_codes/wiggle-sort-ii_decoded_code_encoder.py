class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        sorted_nums = self.copy_of_sorted(nums)
        n = len(nums)
        left = (n - 1) // 2
        right = n - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = sorted_nums[left]
                left -= 1
            else:
                nums[i] = sorted_nums[right]
                right -= 1

    def copy_of_sorted(self, nums):
        return nums[:]