from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)
        for index in range(32):
            count_ones = 0
            for number in nums:
                if (number >> index) & 1 == 1:
                    count_ones += 1
            count_zeros = n - count_ones
            total_distance += count_ones * count_zeros
        return total_distance