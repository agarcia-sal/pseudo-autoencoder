class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count_to_x_or_less = 0
            for value in nums:
                if value <= x:
                    count_to_x_or_less += 1
            return count_to_x_or_less > x

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if f(mid):
                right = mid
            else:
                left = mid + 1
        return left