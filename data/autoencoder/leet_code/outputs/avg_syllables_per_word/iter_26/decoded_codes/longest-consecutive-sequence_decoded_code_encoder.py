class Solution:
    def longestConsecutive(self, list_of_numbers):
        if not list_of_numbers:
            return 0

        number_set = set(list_of_numbers)
        longest_streak = 0

        for number in number_set:
            if number - 1 not in number_set:
                current_number = number
                current_streak = 1

                while current_number + 1 in number_set:
                    current_number += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak