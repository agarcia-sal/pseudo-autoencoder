from collections import Counter
from typing import List

class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        freq = Counter(nums)
        max_freq = max(freq.values())
        return len(nums) // k >= max_freq