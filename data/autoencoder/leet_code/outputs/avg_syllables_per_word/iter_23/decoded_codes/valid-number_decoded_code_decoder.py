import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Pattern explanation:
        # ^[+-]? : optional sign at start
        # (?:     : non-capturing group for the number:
        #    \d+(\.\d*)? : digits, optional decimal point and digits
        #   |            : or
        #    \.\d+        : decimal point followed by digits
        # )
        # (?:[eE][+-]?\d+)? : optional exponent part
        # $ : end of string
        pattern = r'^[+-]?(?:\d+(\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$'
        return re.fullmatch(pattern, s) is not None