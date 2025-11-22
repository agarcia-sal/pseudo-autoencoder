from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, n2 = 0, 0
        m1, m2 = 0, 1  # initialized differently to avoid immediate equality
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

        threshold = len(nums) // 3
        result = []
        if nums.count(m1) > threshold:
            result.append(m1)
        if m2 != m1 and nums.count(m2) > threshold:
            result.append(m2)
        return result