from typing import List

def generate_phone_map() -> dict:
    return {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phone_map = generate_phone_map()
        output = []

        def backtrack(combination: str, next_digits: str):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        backtrack("", digits)
        return output