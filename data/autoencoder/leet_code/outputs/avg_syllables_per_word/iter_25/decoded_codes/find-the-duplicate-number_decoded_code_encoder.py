class Solution:
    def findDuplicate(self, nums):
        def f(x):
            count = 0
            for v in nums:
                if v <= x:
                    count += 1
            return count > x

        length = len(nums)
        left, right = 0, length - 1
        result = -1
        # Binary search for the smallest x where f(x) is True
        while left <= right:
            mid = (left + right) // 2
            if f(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result