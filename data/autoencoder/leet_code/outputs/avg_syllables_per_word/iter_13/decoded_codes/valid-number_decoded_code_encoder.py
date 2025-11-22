import re

class Solution:
    def isNumber(self, s: str) -> bool:
        if s is None:
            return False
        number_regex = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return re.fullmatch(number_regex, s) is not None