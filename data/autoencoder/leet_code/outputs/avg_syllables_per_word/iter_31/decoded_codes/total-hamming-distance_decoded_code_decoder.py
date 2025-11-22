from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)
        for i in range(32):
            count_ones = 0
            for num in nums:
                bit_value = (num >> i) & 1
                count_ones += bit_value
            count_zeros = n - count_ones
            total_distance += count_ones * count_zeros
        return total_distance