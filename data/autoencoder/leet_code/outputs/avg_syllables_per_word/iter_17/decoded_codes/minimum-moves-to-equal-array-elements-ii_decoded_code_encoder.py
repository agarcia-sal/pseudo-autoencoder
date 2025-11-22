class Solution:
    def minMoves2(self, list_of_numbers):
        list_of_numbers.sort()
        middle_index = len(list_of_numbers) // 2
        median_value = list_of_numbers[middle_index]
        total_moves = 0
        for number in list_of_numbers:
            total_moves += abs(number - median_value)
        return total_moves