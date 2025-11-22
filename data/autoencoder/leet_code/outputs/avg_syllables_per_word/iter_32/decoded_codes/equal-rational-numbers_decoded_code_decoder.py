from typing import List

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        # Precomputed ratios for repeating decimal conversion: 1/9, 1/99, 1/999, 1/9999
        ratios: List[float] = [1/9, 1/99, 1/999, 1/9999]

        def valueOf(s: str) -> float:
            leftParenIndex = s.find('(')
            if leftParenIndex == -1:
                # No repeating part, convert directly to float
                return float(s)

            rightParenIndex = s.find(')')
            dotIndex = s.find('.')

            # Floating point number from integer part and non-repeating decimal part
            integerAndNonRepeating = float(s[:leftParenIndex])

            # Length of the non-repeating decimal part
            nonRepeatingLength = leftParenIndex - dotIndex - 1

            # Integer value of the repeating part substring
            repeating_str = s[leftParenIndex + 1:rightParenIndex]
            repeating = int(repeating_str)
            repeatingLength = rightParenIndex - leftParenIndex - 1

            # The formula:
            # result = integerAndNonRepeating + (repeating * 10^(-nonRepeatingLength)) * ratio_for_length
            # where ratio_for_length = 1/9, 1/99, 1/999, or 1/9999 depending on repeatingLength
            return integerAndNonRepeating + repeating * (10 ** -nonRepeatingLength) * ratios[repeatingLength - 1]

        return abs(valueOf(s) - valueOf(t)) < 1e-9