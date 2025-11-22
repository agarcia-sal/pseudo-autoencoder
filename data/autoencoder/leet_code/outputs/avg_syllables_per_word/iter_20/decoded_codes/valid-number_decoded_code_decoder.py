import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(
            r'^[\+\-]?('
            r'(\d+(\.\d*)?)|'
            r'(\.\d+)'
            r')([eE][\+\-]?\d+)?$'
        )
        return bool(pattern.fullmatch(s))