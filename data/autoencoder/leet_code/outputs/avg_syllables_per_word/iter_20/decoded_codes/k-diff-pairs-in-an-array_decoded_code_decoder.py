from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        num_counts = Counter(nums)

        unique_pairs = 0
        if k == 0:
            for count in num_counts.values():
                if count > 1:
                    unique_pairs += 1
        else:
            for num in num_counts:
                if num + k in num_counts:
                    unique_pairs += 1

        return unique_pairs