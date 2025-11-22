class Solution:
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        frequency_list = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                position = (i % sideLength) * sideLength + (j % sideLength)
                frequency_list[position] += 1
        frequency_list.sort(reverse=True)
        total_sum = sum(frequency_list[:maxOnes])
        return total_sum