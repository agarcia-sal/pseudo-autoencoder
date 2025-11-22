class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            if n == 1:
                yield frag
                return
            if frag[0] == '0' and frag[-1] == '0':
                return
            if frag[0] == '0':
                yield '0.' + frag[1:]
                return
            if frag[-1] == '0':
                yield frag
                return
            yield frag
            for d in range(1, n):
                yield frag[:d] + '.' + frag[d:]

        s = s[1:-1]
        res = []
        for i in range(1, len(s)):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    res.append(f'({a}, {b})')
        return res