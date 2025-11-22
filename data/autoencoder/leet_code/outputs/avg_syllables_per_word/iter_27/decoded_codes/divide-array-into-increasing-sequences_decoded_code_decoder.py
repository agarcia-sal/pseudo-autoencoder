from collections import Counter
from typing import List

class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)
        max_freq = max(freq.values(), default=0)
        length_of_nums = len(nums)
        division_result = length_of_nums // k
        return division_result >= max_freq