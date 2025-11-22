class Solution:
    def majorityElement(self, nums):
        n1, n2 = 0, 0
        m1, m2 = 0, 1  # initialize m1 and m2 to different values to avoid initial conflict
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
        return [m for m in (m1, m2) if nums.count(m) > len(nums) // 3]