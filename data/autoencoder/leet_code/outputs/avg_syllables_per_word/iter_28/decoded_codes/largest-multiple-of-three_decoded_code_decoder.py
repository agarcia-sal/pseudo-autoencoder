from collections import Counter
from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        count = Counter(digits)
        total_sum = sum(digits)
        remainder = total_sum % 3

        if remainder == 1:
            for d in (1, 4, 7):
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                for d in (2, 5, 8):
                    if count[d] > 1:
                        count[d] -= 2
                        break
        elif remainder == 2:
            for d in (2, 5, 8):
                if count[d] > 0:
                    count[d] -= 1
                    break
            else:
                for d in (1, 4, 7):
                    if count[d] > 1:
                        count[d] -= 2
                        break

        result = []
        for digit in range(9, -1, -1):
            result.extend([str(digit)] * count[digit])

        if not result:
            return ""

        if result[0] == '0':
            return "0"

        return "".join(result)