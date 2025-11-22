from collections import defaultdict
from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        pair_and_count = defaultdict(int)

        for i in nums:
            for j in nums:
                key = i & j
                pair_and_count[key] += 1

        triplet_count = 0
        for k in nums:
            for pair_and, count in pair_and_count.items():
                if (pair_and & k) == 0:
                    triplet_count += count

        return triplet_count