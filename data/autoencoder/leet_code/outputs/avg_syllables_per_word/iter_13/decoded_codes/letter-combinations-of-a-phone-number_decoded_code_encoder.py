class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []

        phone_map = {
            '2': "ABC",
            '3': "DEF",
            '4': "GHI",
            '5': "JKL",
            '6': "MNO",
            '7': "PQRS",
            '8': "TUV",
            '9': "WXYZ"
        }

        output = []

        def backtrack(combination: str, next_digits: str):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return output