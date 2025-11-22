from typing import List, Generator

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> Generator[str, None, None]:
            n = len(frag)
            # Try all possible splits for decimal placement
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Skip invalid numbers according to problem's rules:
                # Left part cannot start with '0' unless it is exactly '0'
                # Right part cannot end with '0' if it exists (to avoid trailing zeros after decimal)
                if (left == "0" or not left.startswith("0")) and (not right or not right.endswith("0")):
                    yield left + ('.' + right if right else '')

        s = s[1:-1]  # Remove outer parentheses
        res = []
        for i in range(1, len(s)):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    res.append(f"({a}, {b})")
        return res