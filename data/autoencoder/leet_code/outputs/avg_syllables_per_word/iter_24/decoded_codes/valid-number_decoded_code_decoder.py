import re

class Solution:
    def isNumber(self, s):
        pattern = r'^[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$'
        return bool(re.fullmatch(pattern, s))