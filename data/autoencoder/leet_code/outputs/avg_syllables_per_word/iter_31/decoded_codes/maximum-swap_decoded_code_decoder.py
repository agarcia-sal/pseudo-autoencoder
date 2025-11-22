from typing import Dict

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last: Dict[int, int] = {}

        # Record the last occurrence of each digit
        for i, d in enumerate(digits):
            digit_value = int(d)
            last[digit_value] = i

        # Try to find a digit to swap with a larger digit occurring later
        for i, d in enumerate(digits):
            digit_value = int(d)
            for d2 in range(9, digit_value, -1):
                if d2 in last and last[d2] > i:
                    pos = last[d2]
                    digits[i], digits[pos] = digits[pos], digits[i]
                    return int(''.join(digits))
        return num