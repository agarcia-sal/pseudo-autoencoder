from typing import Dict, List

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits: List[str] = list(str(num))
        last: Dict[int, int] = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            current_digit = int(d)
            for digit2 in range(9, current_digit, -1):
                if digit2 in last and last[digit2] > i:
                    j = last[digit2]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        return num