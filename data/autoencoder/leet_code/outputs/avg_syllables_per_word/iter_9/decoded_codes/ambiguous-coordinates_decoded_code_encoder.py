class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n + 1):
                left, right = frag[:d], frag[d:]
                if (left == "0" or not left.startswith("0")) and (not right.endswith("0")):
                    yield left + ("" if d == n else ".") + right

        s = s[1:-1]
        return [
            f"({a}, {b})"
            for i in range(1, len(s))
            for a in make(s[:i])
            for b in make(s[i:])
        ]