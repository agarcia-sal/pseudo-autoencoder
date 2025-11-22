from typing import List

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        frequency = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                position = (i % sideLength) * sideLength + (j % sideLength)
                frequency[position] += 1

        frequency.sort(reverse=True)
        return sum(frequency[:maxOnes])