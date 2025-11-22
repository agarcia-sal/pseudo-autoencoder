from collections import Counter
from math import isqrt
from typing import List

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(n: int) -> bool:
            root = isqrt(n)
            return root * root == n

        def backtrack(path: List[int], count: Counter) -> int:
            if len(path) == len(nums):
                return 1
            ans = 0
            for x in count:
                if count[x] > 0 and (not path or is_square(path[-1] + x)):
                    count[x] -= 1
                    ans += backtrack(path + [x], count)
                    count[x] += 1
            return ans

        count = Counter(nums)
        return backtrack([], count)