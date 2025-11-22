from typing import List


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios: List[float] = [1, 1/9, 1/99, 1/999, 1/9999]

        def valueOf(num: str) -> float:
            leftParenIndex = num.find('(')
            if leftParenIndex == -1:
                return float(num)

            rightParenIndex = num.find(')')
            dotIndex = num.find('.')

            integer_and_non_repeating = float(num[:leftParenIndex - 1])
            non_repeating_length = leftParenIndex - dotIndex - 1

            repeating = int(num[leftParenIndex + 1:rightParenIndex])
            repeating_length = rightParenIndex - leftParenIndex - 1

            return integer_and_non_repeating + repeating * (10 ** (-non_repeating_length)) * ratios[repeating_length]

        return abs(valueOf(s) - valueOf(t)) < 1e-9