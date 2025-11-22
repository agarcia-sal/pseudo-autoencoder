class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        sum_ab = {}
        for a in nums1:
            for b in nums2:
                sum_ab[a + b] = sum_ab.get(a + b, 0) + 1

        count = 0
        for c in nums3:
            for d in nums4:
                count += sum_ab.get(-(c + d), 0)

        return count