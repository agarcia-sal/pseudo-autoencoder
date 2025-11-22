class Solution:
    def minimumMountainRemovals(self, list_of_numbers):
        length_n = len(list_of_numbers)

        longest_increasing_subsequence = [1] * length_n
        for i in range(length_n):
            for j in range(i):
                if list_of_numbers[i] > list_of_numbers[j]:
                    longest_increasing_subsequence[i] = max(
                        longest_increasing_subsequence[i], longest_increasing_subsequence[j] + 1
                    )

        longest_decreasing_subsequence = [1] * length_n
        for i in range(length_n - 1, -1, -1):
            for j in range(i + 1, length_n):
                if list_of_numbers[i] > list_of_numbers[j]:
                    longest_decreasing_subsequence[i] = max(
                        longest_decreasing_subsequence[i], longest_decreasing_subsequence[j] + 1
                    )

        maximum_mountain_length = 0
        for i in range(1, length_n - 1):
            if longest_increasing_subsequence[i] > 1 and longest_decreasing_subsequence[i] > 1:
                current_length = longest_increasing_subsequence[i] + longest_decreasing_subsequence[i] - 1
                if current_length > maximum_mountain_length:
                    maximum_mountain_length = current_length

        minimum_number_of_removals = length_n - maximum_mountain_length
        return minimum_number_of_removals