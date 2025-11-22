class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                if (left == "0" or not left.startswith("0")):
                    if not right.endswith("0"):
                        yield left + (("." + right) if d != n else "")
        s = s[1:-1]
        res = []
        for i in range(1, len(s)):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    res.append(f"({a}, {b})")
        return res