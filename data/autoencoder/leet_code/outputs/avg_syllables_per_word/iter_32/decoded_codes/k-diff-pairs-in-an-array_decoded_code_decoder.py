from collections import Counter
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        num_counts = Counter(nums)
        unique_pairs = 0

        if k == 0:
            # Count numbers that appear more than once
            for count in num_counts.values():
                if count > 1:
                    unique_pairs += 1
        else:
            # For k > 0, check existence of num + k
            for num in num_counts:
                if num + k in num_counts:
                    unique_pairs += 1

        return unique_pairs