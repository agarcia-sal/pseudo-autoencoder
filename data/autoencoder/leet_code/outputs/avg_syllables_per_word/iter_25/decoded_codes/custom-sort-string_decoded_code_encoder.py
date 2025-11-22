class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        sorted_characters = sorted(s, key=lambda x: d.get(x, 0))
        return ''.join(sorted_characters)