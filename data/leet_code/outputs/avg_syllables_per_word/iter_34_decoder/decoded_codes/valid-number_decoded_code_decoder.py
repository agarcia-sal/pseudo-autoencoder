import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?$'
        return re.fullmatch(pattern, s) is not None