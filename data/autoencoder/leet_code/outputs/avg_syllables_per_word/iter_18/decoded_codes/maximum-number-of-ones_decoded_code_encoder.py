class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        frequency_list = [0] * (sideLength * sideLength)
        for i in range(width):
            for j in range(height):
                position_in_submatrix = (i % sideLength) * sideLength + (j % sideLength)
                frequency_list[position_in_submatrix] += 1
        frequency_list.sort(reverse=True)
        sum_of_top_frequencies = sum(frequency_list[:maxOnes])
        return sum_of_top_frequencies