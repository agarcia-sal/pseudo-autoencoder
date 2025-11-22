import re

class Solution:
    def isNumber(self, s: str) -> bool:
        number_regex = r"^[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$"
        return bool(re.fullmatch(number_regex, s))