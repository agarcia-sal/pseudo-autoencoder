from typing import List, Iterator, Tuple
from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> Iterator[str]:
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Check conditions for valid coordinates
                if (left == '0' or not left.startswith('0')) and (not right.endswith('0')):
                    if d != n:
                        yield left + '.' + right
                    else:
                        yield left

        s = s[1:-1]
        result = []
        for i in range(1, len(s)):
            left_frag = s[:i]
            right_frag = s[i:]
            for a, b in product(make(left_frag), make(right_frag)):
                result.append(f"({a}, {b})")
        return result