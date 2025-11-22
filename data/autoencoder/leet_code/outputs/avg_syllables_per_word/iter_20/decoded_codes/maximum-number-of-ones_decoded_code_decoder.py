from typing import List

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        frequency_list: List[int] = [0] * (sideLength * sideLength)
        for i in range(width):
            i_mod = i % sideLength
            base = i_mod * sideLength
            for j in range(height):
                position = base + (j % sideLength)
                frequency_list[position] += 1
        frequency_list.sort(reverse=True)
        return sum(frequency_list[:maxOnes])