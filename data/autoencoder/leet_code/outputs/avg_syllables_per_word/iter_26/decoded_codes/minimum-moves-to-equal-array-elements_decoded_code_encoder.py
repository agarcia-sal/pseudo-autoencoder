class Solution:
    def minMoves(self, list_of_numbers):
        minimum_number = min(list_of_numbers)
        return sum(num - minimum_number for num in list_of_numbers)