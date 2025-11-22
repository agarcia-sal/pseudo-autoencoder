from typing import List, Iterator, Tuple
from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> Iterator[str]:
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                if (not left.startswith('0') or left == '0') and (not right.endswith('0')):
                    yield left + ('.' if d != n else '') + right
        s = s[1:-1]
        return [f"({a}, {b})" for i in range(1, len(s)) for a, b in product(make(s[:i]), make(s[i:]))]