class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count_le = sum(v <= x for v in nums)
            count_g = sum(v > x for v in nums)
            return count_le > count_g

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left