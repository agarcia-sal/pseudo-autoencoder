from math import gcd
from functools import reduce

def isGoodArray(nums):
    return reduce(gcd, nums) == 1