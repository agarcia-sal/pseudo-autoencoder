class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        freq = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                pos = (i % sideLength) * sideLength + (j % sideLength)
                freq[pos] += 1
        freq.sort(reverse=True)
        result = sum(freq[:maxOnes])
        return result