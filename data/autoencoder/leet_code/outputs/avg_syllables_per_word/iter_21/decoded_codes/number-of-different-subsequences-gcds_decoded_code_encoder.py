from math import gcd
from typing import List

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        num_set = set(nums)
        count = 0

        for g in range(1, max_num + 1):
            gcd_val = 0
            for m in range(g, max_num + 1, g):
                if m in num_set:
                    gcd_val = gcd(gcd_val, m)
                    if gcd_val == g:
                        count += 1
                        break
        return count