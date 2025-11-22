class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        freq = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                rowPosition = i % sideLength
                columnPosition = j % sideLength
                pos = rowPosition * sideLength + columnPosition
                freq[pos] += 1
        freq.sort(reverse=True)
        total_ONES = sum(freq[:maxOnes])
        return total_ONES