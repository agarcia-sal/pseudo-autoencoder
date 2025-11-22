class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # left cannot start with '0' unless left == '0'
                # right cannot end with '0' if right is not empty
                if (left[0] != '0' or left == '0') and (not right or right[-1] != '0'):
                    yield left + ('.' if d != n else '') + right

        s = s[1:-1]
        res = []
        n = len(s)
        for i in range(1, n):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    res.append(f'({a}, {b})')
        return res