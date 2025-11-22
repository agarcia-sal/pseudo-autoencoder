class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MODULO = 10**9 + 7
        length_of_num = len(num)
        memoization_dictionary = {}

        def dp(current_index: int, previous_length: int) -> int:
            if current_index == length_of_num:
                return 1

            key = (current_index, previous_length)
            if key in memoization_dictionary:
                return memoization_dictionary[key]

            count_of_combinations = 0
            for length_from_one in range(1, length_of_num - current_index + 1):
                if num[current_index] == '0':
                    break

                current_number_substring = num[current_index:current_index + length_from_one]
                if previous_length == 0:
                    valid = True
                else:
                    prev_start = current_index - previous_length
                    prev_substring = num[prev_start:current_index]

                    # To compare numbers as strings accurately when lengths are different,
                    # first check lengths, if same compare lex order
                    if len(prev_substring) == len(current_number_substring):
                        valid = current_number_substring >= prev_substring
                    elif len(current_number_substring) > len(prev_substring):
                        valid = True
                    else:
                        valid = False

                if valid:
                    count_of_combinations += dp(current_index + length_from_one, length_from_one)
                    count_of_combinations %= MODULO

            memoization_dictionary[key] = count_of_combinations
            return count_of_combinations

        return dp(0, 0)