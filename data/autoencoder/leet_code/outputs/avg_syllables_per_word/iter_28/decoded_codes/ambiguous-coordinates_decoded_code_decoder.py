from typing import List, Iterator
from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> Iterator[str]:
            n = len(frag)
            if n == 1:
                yield frag
                return
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Conditions:
                # left should not start with '0' unless left == "0"
                # right should not end with '0'
                if (left[0] != '0' or left == "0") and (not right or right[-1] != '0'):
                    yield left + ('.' + right if d != n else '')

        s = s[1:-1]
        result = []
        for i in range(1, len(s)):
            left_frag = s[:i]
            right_frag = s[i:]
            for a, b in product(make(left_frag), make(right_frag)):
                result.append(f"({a}, {b})")
        return result