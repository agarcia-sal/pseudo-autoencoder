from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)
        for i in range(32):  # iterate over each bit position
            count_ones = 0
            for num in nums:
                # Check if the i-th bit is set (1) in num
                if (num >> i) & 1:
                    count_ones += 1
            count_zeros = n - count_ones
            total_distance += count_ones * count_zeros
        return total_distance