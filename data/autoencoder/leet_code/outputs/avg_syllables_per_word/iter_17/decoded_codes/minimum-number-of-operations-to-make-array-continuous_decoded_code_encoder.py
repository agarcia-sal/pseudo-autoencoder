class Solution:
    def minOperations(self, list_of_numbers):
        n = len(list_of_numbers)
        unique_numbers = sorted(set(list_of_numbers))
        minimum_operations = n
        pointer_j = 0
        length_unique = len(unique_numbers)
        for index_i in range(length_unique):
            while pointer_j < length_unique and unique_numbers[pointer_j] < unique_numbers[index_i] + n:
                pointer_j += 1
            minimum_operations = min(minimum_operations, n - (pointer_j - index_i))
        return minimum_operations