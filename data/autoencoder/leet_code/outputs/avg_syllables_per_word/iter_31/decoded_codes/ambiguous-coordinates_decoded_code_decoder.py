from typing import List, Generator

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> Generator[str, None, None]:
            n = len(frag)
            # Generate all valid representations of fragment as a decimal number,
            # either integer or with decimal point placed at d-th position.
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Check validity rules:
                # left part is valid if it's a single '0' or does not start with '0'.
                if (left == "0" or left[0] != '0') and (right == "" or right[-1] != '0'):
                    # If no right part, no decimal point; else insert decimal point
                    yield left + ('.' + right if right else '')

        s = s[1:-1]  # Remove the surrounding parentheses
        res = []
        length = len(s)
        for i in range(1, length):
            left_frag = s[:i]
            right_frag = s[i:]
            # Generate all possible valid numbers from left_frag and right_frag
            for a in make(left_frag):
                for b in make(right_frag):
                    res.append(f"({a}, {b})")
        return res