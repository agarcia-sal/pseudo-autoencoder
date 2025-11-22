from typing import List

class Solution:
    def totalHammingDistance(self, list_of_numbers: List[int]) -> int:
        total_distance = 0
        n = len(list_of_numbers)
        for bit_position in range(32):
            count_ones = 0
            for number in list_of_numbers:
                count_ones += (number >> bit_position) & 1
            count_zeros = n - count_ones
            total_distance += count_ones * count_zeros
        return total_distance