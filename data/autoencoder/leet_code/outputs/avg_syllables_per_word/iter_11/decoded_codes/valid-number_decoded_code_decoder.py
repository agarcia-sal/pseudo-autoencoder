import re

class Solution:
    def isNumber(self, s: str) -> bool:
        number_pattern = r'^[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$'
        return bool(re.fullmatch(number_pattern, s))