from collections import Counter
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums):
        def is_square(n):
            r = isqrt(n)
            return r * r == n

        count = Counter(nums)
        nums_unique = list(count.keys())
        n = len(nums)

        def backtrack(path, count):
            if len(path) == n:
                return 1
            ans = 0
            for x in nums_unique:
                if count[x] > 0 and (not path or is_square(path[-1] + x)):
                    count[x] -= 1
                    ans += backtrack(path + [x], count)
                    count[x] += 1
            return ans

        return backtrack([], count)