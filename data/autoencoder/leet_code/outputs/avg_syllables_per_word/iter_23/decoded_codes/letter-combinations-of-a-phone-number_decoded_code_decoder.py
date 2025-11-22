from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        output = []

        def backtrack(combination_string: str, next_digits_string: str) -> None:
            if len(next_digits_string) == 0:
                output.append(combination_string)
            else:
                for letter_character in phone_map[next_digits_string[0]]:
                    backtrack(combination_string + letter_character, next_digits_string[1:])

        backtrack("", digits)
        return output