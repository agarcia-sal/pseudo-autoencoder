import re

class Solution:
    def isNumber(self, input_string: str) -> bool:
        number_pattern = re.compile(
            r'^[\+\-]?('
            r'(\d+(\.\d*)?)|'      # digits followed by optional decimal point and digits
            r'(\.\d+)'             # decimal point followed by digits
            r')([eE][\+\-]?\d+)?$' # optional exponent part
        )
        return number_pattern.match(input_string) is not None