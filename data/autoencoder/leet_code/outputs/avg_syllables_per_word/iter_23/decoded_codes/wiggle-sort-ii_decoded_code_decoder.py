class Solution:
    def wiggleSort(self, nums) -> None:
        sortedNums = sorted(nums)
        n = len(nums)
        left = (n - 1) // 2
        right = n - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = sortedNums[left]
                left -= 1
            else:
                nums[i] = sortedNums[right]
                right -= 1