from typing import Dict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d: Dict[str, int] = {}
        for i, c in enumerate(order):
            d[c] = i
        sorted_characters = sorted(s, key=lambda x: d[x] if x in d else 0)
        result = ''.join(sorted_characters)
        return result