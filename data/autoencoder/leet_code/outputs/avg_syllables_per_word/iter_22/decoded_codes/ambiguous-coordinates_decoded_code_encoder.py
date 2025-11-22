class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Check if left is a valid integer part (no leading zeros unless it's zero)
                if not (left[0] == '0' and len(left) > 1):
                    # If right is empty, yield left without decimal
                    if not right:
                        yield left
                    # If right is non-empty, must not end with zero (for decimal part)
                    elif right[-1] != '0':
                        yield left + '.' + right

        s = s[1:-1]  # remove the enclosing parentheses
        result = []
        for i in range(1, len(s)):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    result.append(f"({a}, {b})")
        return result