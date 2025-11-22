import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regex pattern to match a valid number according to the given specification:
        # Optional '+' or '-' sign
        # Followed by either:
        #   - One or more digits, optionally followed by a decimal point and zero or more digits
        #   OR
        #   - A decimal point followed by one or more digits
        # Followed by an optional exponent part:
        #   'e' followed by optional '+' or '-' sign and one or more digits
        number_regular_expression = re.compile(
            r'^[\+\-]?('
            r'(\d+(\.\d*)?)|'
            r'(\.\d+)'
            r')([eE][\+\-]?\d+)?$'
        )
        return bool(number_regular_expression.fullmatch(s))