from collections import Counter

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        sum_ab = Counter(a + b for a in nums1 for b in nums2)
        count = 0
        for c in nums3:
            for d in nums4:
                target = - (c + d)
                count += sum_ab.get(target, 0)
        return count