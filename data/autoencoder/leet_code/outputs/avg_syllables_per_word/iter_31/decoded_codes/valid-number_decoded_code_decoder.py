import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(
            r'^[+-]?('
            r'(\d+(\.\d*)?)|'  # digits followed by optional decimal point and optional digits
            r'(\.\d+)'          # decimal point followed by digits
            r')'
            r'([eE][+-]?\d+)?$'  # optional exponent part
        )
        return bool(pattern.match(s))