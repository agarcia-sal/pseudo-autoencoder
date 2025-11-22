class Solution:
    def majorityElement(self, nums):
        n1 = n2 = 0
        m1 = m2 = None
        for m in nums:
            if m == m1:
                n1 += 1
            elif m == m2:
                n2 += 1
            elif n1 == 0:
                m1, n1 = m, 1
            elif n2 == 0:
                m2, n2 = m, 1
            else:
                n1 -= 1
                n2 -= 1
        return [m for m in (m1, m2) if m is not None and nums.count(m) > len(nums) // 3]