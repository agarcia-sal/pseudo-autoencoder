from collections import Counter
from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        if remainder == 1:
            for digit in (1, 4, 7):
                if count[digit] > 0:
                    count[digit] -= 1
                    break
            else:
                for digit in (2, 5, 8):
                    if count[digit] > 1:
                        count[digit] -= 2
                        break
        elif remainder == 2:
            for digit in (2, 5, 8):
                if count[digit] > 0:
                    count[digit] -= 1
                    break
            else:
                for digit in (1, 4, 7):
                    if count[digit] > 1:
                        count[digit] -= 2
                        break

        result = []
        for digit in range(9, -1, -1):
            if count[digit] > 0:
                result.append(str(digit) * count[digit])

        final_number = ''.join(result)

        if len(final_number) > 0 and final_number[0] == '0':
            return '0'
        return final_number