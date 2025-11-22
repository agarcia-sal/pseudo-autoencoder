class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        conversion_map = {}

        for c1, c2 in zip(str1, str2):
            if c1 in conversion_map:
                if conversion_map[c1] != c2:
                    return False
            else:
                conversion_map[c1] = c2

        if len(set(str2)) == 26:
            return False

        return True