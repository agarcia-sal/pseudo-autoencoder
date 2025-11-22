from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        def f(x: int) -> bool:
            count = 0
            for value in nums:
                if value <= x:
                    count += 1
            return count > x

        search_range = range(len(nums))
        result = bisect_left(search_range, True, key=f)
        return result