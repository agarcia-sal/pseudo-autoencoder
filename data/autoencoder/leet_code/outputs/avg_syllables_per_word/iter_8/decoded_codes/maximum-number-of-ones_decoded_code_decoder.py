class Solution:
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        freq = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                pos = (i % sideLength) * sideLength + (j % sideLength)
                freq[pos] += 1

        freq.sort(reverse=True)
        result = sum(freq[:maxOnes])
        return result