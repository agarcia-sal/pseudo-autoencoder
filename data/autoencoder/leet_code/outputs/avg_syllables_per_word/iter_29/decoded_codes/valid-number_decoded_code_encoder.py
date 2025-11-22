import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Pattern matches optional sign, digits with optional decimal part,
        # optional exponent with optional sign and digits
        pattern = re.compile(r'^[\+\-]?(\d+(\.\d*)?|\.\d+)([eE][\+\-]?\d+)?$')
        return bool(pattern.match(s.strip()))