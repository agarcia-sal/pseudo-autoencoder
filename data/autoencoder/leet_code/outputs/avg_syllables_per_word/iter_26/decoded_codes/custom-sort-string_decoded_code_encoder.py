class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        sorted_characters = sorted(s, key=lambda c: d.get(c, 0))
        result = ''.join(sorted_characters)
        return result