class Solution:
    def getXORSum(self, arr1, arr2):
        xor_sum_arr1 = 0
        for number in arr1:
            xor_sum_arr1 ^= number
        xor_sum_arr2 = 0
        for number in arr2:
            xor_sum_arr2 ^= number
        return xor_sum_arr1 & xor_sum_arr2