from typing import List

class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        freq = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                row_position = i % sideLength
                column_position = j % sideLength
                pos = row_position * sideLength + column_position
                freq[pos] += 1

        freq.sort(reverse=True)
        result = sum(freq[:maxOnes])
        return result