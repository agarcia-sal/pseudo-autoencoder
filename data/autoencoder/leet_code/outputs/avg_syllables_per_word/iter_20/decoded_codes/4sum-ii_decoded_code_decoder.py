from collections import Counter
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_ab = Counter()
        for a in nums1:
            for b in nums2:
                sum_ab[a + b] += 1

        count = 0
        for c in nums3:
            for d in nums4:
                target = - (c + d)
                count += sum_ab.get(target, 0)
        return count