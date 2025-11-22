from typing import Dict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d: Dict[str, int] = {}
        for i in range(len(order)):
            character = order[i]
            value = i
            d[character] = value
        # Characters not in d get value -1 so they come after those in d
        sorted_characters = sorted(s, key=lambda x: d.get(x, -1))
        result_string = "".join(sorted_characters)
        return result_string