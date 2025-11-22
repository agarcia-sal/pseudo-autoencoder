from math import gcd
from functools import reduce
from typing import List

class Solution:
    def isGoodArray(self, list_of_numbers: List[int]) -> bool:
        total_gcd = reduce(gcd, list_of_numbers)
        return total_gcd == 1