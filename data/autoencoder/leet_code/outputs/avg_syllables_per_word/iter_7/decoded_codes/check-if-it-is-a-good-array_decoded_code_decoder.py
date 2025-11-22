from math import gcd
from functools import reduce
from typing import List

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        total_gcd = reduce(gcd, nums)
        return total_gcd == 1