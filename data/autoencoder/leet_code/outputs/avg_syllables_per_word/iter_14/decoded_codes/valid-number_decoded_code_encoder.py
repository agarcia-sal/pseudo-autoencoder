import re

class Solution:
    def isNumber(self, s: str) -> bool:
        number_pattern = re.compile(
            r'^[\+\-]?('                            # optional sign
            r'(\d+(\.\d*)?)|'                       # digits with optional decimal and optional digits
            r'(\.\d+)'                             # decimal with digits
            r')([eE][\+\-]?\d+)?$'                  # optional exponent
        )
        return bool(number_pattern.match(s))