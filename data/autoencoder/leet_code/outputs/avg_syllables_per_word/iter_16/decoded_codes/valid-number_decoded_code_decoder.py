import re

class Solution:
    def isNumber(self, s: str) -> bool:
        number_regex = r'^[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$'
        return re.fullmatch(number_regex, s) is not None