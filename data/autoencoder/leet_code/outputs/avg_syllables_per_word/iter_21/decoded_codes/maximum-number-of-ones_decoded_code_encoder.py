class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        freq = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                position = (i % sideLength) * sideLength + (j % sideLength)
                freq[position] += 1
        freq.sort(reverse=True)
        total = sum(freq[:maxOnes])
        return total