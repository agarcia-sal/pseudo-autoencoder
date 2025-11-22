class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda c: d.get(c, 0)))