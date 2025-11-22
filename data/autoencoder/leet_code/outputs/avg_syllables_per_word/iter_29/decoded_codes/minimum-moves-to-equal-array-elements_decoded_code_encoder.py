class Solution:
    def minMoves(self, list_of_numbers):
        minimum_number = min(list_of_numbers)
        total_moves = 0
        for number in list_of_numbers:
            total_moves += number - minimum_number
        return total_moves