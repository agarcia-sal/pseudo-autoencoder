from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, n2 = 0, 0
        m1, m2 = 0, 1  # Initialize with distinct arbitrary values
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

        result_list = []
        for candidate in (m1, m2):
            if nums.count(candidate) > len(nums) // 3:
                if candidate not in result_list:
                    result_list.append(candidate)
        return result_list