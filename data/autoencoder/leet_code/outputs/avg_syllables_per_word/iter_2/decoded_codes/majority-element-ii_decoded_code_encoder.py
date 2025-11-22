class Solution:
    def majorityElement(self, nums):
        n1, n2 = 0, 0
        m1, m2 = 0, 1

        for m in nums:
            if m == m1:
                n1 += 1
            elif m == m2:
                n2 += 1
            elif n1 == 0:
                m1 = m
                n1 = 1
            elif n2 == 0:
                m2 = m
                n2 = 1
            else:
                n1 -= 1
                n2 -= 1

        result = []
        for m in [m1, m2]:
            if nums.count(m) > len(nums) // 3:
                result.append(m)
        return result