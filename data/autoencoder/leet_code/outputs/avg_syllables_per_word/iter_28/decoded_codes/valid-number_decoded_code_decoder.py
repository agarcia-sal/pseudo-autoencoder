import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r'^[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$', re.IGNORECASE)
        return bool(pattern.fullmatch(s))