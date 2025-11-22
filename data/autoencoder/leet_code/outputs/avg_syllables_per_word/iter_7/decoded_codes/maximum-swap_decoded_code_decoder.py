from typing import Dict, List

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits: List[str] = list(str(num))
        last: Dict[int, int] = {}

        for i, d in enumerate(digits):
            last[int(d)] = i

        for i, d in enumerate(digits):
            for d2 in range(9, int(d), -1):
                if d2 in last and last[d2] > i:
                    digits[i], digits[last[d2]] = digits[last[d2]], digits[i]
                    result = int("".join(digits))
                    return result
        return num