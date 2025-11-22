from typing import Generator, List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> Generator[str, None, None]:
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                if (left == "0" or not left.startswith('0')) and (right == "" or not right.endswith('0')):
                    yield left + ('.' + right if d != n else "")

        s = s[1:-1]
        result = []
        for i in range(1, len(s)):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    result.append(f"({a}, {b})")
        return result