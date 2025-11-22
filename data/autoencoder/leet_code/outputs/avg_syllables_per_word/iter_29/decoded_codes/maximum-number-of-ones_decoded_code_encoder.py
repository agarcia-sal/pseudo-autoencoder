class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        frequency_list = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                position = (i % sideLength) * sideLength + (j % sideLength)
                frequency_list[position] += 1
        frequency_list.sort(reverse=True)
        return sum(frequency_list[:maxOnes])