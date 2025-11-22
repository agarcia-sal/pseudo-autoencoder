class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        xor_sum_arr1 = 0
        for num in arr1:
            xor_sum_arr1 ^= num
        xor_sum_arr2 = 0
        for num in arr2:
            xor_sum_arr2 ^= num
        result = xor_sum_arr1 & xor_sum_arr2
        return result