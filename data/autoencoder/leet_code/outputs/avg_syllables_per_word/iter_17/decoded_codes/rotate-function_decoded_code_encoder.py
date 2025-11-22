class Solution:
    def maxRotateFunction(self, list_of_numbers):
        length_n = len(list_of_numbers)
        if length_n == 1:
            return 0
        total_sum = sum(list_of_numbers)
        current_sum = sum(i * num for i, num in enumerate(list_of_numbers))
        max_value = current_sum
        for k in range(1, length_n):
            current_sum += total_sum - length_n * list_of_numbers[length_n - k]
            if current_sum > max_value:
                max_value = current_sum
        return max_value