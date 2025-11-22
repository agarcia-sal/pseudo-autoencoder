import re

class Solution:
    def isNumber(self, s):
        number_pattern = re.compile(
            r'^[\+\-]?('
            r'(\d+(\.\d*)?)|'
            r'(\.\d+)'
            r')([eE][\+\-]?\d+)?$'
        )
        return bool(number_pattern.match(s))