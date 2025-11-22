from typing import Dict

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last: Dict[int, int] = {}
        for i, d in enumerate(digits):
            last[int(d)] = i

        for i, d in enumerate(digits):
            current_digit = int(d)
            for digit_to_swap in range(9, current_digit, -1):
                if digit_to_swap in last and last[digit_to_swap] > i:
                    j = last[digit_to_swap]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        return num