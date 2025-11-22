class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        list_of_characters = sorted(s, key=lambda x: d.get(x, 0))
        return ''.join(list_of_characters)