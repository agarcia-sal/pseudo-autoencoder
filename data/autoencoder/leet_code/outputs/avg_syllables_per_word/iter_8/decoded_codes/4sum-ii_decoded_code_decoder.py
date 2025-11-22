class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        sum_ab = {}
        for a in nums1:
            for b in nums2:
                current_sum = a + b
                if current_sum in sum_ab:
                    sum_ab[current_sum] += 1
                else:
                    sum_ab[current_sum] = 1
        count = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_ab:
                    count += sum_ab[target]
        return count