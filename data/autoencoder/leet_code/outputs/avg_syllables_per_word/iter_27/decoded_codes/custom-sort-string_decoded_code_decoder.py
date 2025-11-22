from typing import Dict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d: Dict[str, int] = {}
        for i, c in enumerate(order):
            d[c] = i
        sorted_characters = sorted(s, key=lambda c: d.get(c, 0))
        result_string = ''.join(sorted_characters)
        return result_string