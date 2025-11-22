from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num

        diff_bit = xor_all & (-xor_all)

        num1 = 0
        num2 = 0
        for num in nums:
            if num & diff_bit != 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]