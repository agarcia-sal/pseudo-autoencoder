from math import gcd
from typing import List

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        maximum_number = max(nums)
        number_set = set(nums)
        count = 0

        for g in range(1, maximum_number + 1):
            gcd_value = 0
            for m in range(g, maximum_number + 1, g):
                if m in number_set:
                    gcd_value = gcd(gcd_value, m)
                    if gcd_value == g:
                        count += 1
                        break

        return count