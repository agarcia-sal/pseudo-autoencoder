import re

class Solution:
    def isNumber(self, s: str) -> bool:
        number_regex = r'^[\+\-]?(\d+(\.\d*)?|\.\d+)([eE][\+\-]?\d+)?$'
        return re.fullmatch(number_regex, s) is not None