from collections import Counter

class Solution:
    def deleteAndEarn(self, nums):
        count_of_each_number = Counter(nums)
        sorted_unique_numbers = sorted(count_of_each_number)
        length_of_unique_numbers = len(sorted_unique_numbers)
        dp_values = [0] * (length_of_unique_numbers + 1)
        dp_values[1] = sorted_unique_numbers[0] * count_of_each_number[sorted_unique_numbers[0]]

        for i in range(2, length_of_unique_numbers + 1):
            current_number = sorted_unique_numbers[i - 1]
            prev_number = sorted_unique_numbers[i - 2]
            if current_number == prev_number + 1:
                dp_values[i] = max(
                    dp_values[i - 1],
                    dp_values[i - 2] + current_number * count_of_each_number[current_number]
                )
            else:
                dp_values[i] = dp_values[i - 1] + current_number * count_of_each_number[current_number]

        return dp_values[length_of_unique_numbers]