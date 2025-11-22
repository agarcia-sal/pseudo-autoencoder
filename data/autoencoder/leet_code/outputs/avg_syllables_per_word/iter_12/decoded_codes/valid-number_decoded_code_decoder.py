import re

class Solution:
    def isNumber(self, s: str) -> bool:
        number_regex = re.compile(
            r"""^[\+\-]?(
                (\d+(\.\d*)?) |      # Digits with optional fractional part
                (\.\d+)              # Or leading dot with digits
            )
            ([eE][\+\-]?\d+)?$       # Optional exponent part
            """, re.VERBOSE)
        return bool(number_regex.fullmatch(s))