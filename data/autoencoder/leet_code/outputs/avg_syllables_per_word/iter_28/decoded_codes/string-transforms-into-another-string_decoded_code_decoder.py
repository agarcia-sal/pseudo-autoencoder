from typing import Dict

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        conversion_map: Dict[str, str] = {}
        for char1, char2 in zip(str1, str2):
            if char1 in conversion_map:
                if conversion_map[char1] != char2:
                    return False
            else:
                conversion_map[char1] = char2
        if len(set(str2)) == 26:
            return False
        return True