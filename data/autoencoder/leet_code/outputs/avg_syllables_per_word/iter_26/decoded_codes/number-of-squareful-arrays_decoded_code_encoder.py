from collections import Counter
from math import isqrt
from typing import List

class Solution:
    def numSquarefulPerms(self, list_of_numbers: List[int]) -> int:
        def is_square(number: int) -> bool:
            root = isqrt(number)
            return root * root == number

        def backtrack(current_path: List[int], frequency_count: Counter) -> int:
            if len(current_path) == len(list_of_numbers):
                return 1

            answer = 0
            for element in frequency_count:
                if frequency_count[element] > 0 and (not current_path or is_square(current_path[-1] + element)):
                    frequency_count[element] -= 1
                    answer += backtrack(current_path + [element], frequency_count)
                    frequency_count[element] += 1
            return answer

        frequency_count = Counter(list_of_numbers)
        return backtrack([], frequency_count)