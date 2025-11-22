from math import isqrt
from typing import List, Dict

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(n: int) -> bool:
            root = isqrt(n)
            return root * root == n

        def backtrack(path: List[int], count: Dict[int, int]) -> int:
            if len(path) == len(nums):
                return 1

            ans = 0
            for x in count:
                if count[x] > 0 and (not path or is_square(path[-1] + x)):
                    count[x] -= 1
                    ans += backtrack(path + [x], count)
                    count[x] += 1
            return ans

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        return backtrack([], count)