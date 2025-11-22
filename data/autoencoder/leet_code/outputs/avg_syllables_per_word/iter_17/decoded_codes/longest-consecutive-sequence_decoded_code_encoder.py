class Solution:
    def longestConsecutive(self, list_of_numbers):
        if not list_of_numbers:
            return 0

        set_of_numbers = set(list_of_numbers)
        longest_streak = 0

        for number in set_of_numbers:
            if number - 1 not in set_of_numbers:
                current_number = number
                current_streak = 1

                while current_number + 1 in set_of_numbers:
                    current_number += 1
                    current_streak += 1

                if current_streak > longest_streak:
                    longest_streak = current_streak

        return longest_streak