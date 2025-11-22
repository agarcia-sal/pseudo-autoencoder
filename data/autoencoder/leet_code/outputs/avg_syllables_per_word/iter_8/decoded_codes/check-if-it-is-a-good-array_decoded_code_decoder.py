from math import gcd
from functools import reduce

class Solution:
    def isGoodArray(self, nums):
        total_gcd = reduce(gcd, nums)
        if total_gcd == 1:
            return True
        else:
            return False