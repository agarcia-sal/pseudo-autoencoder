import re

class Solution:
    def isNumber(self, s):
        number_pattern = r'^[\+\-]?((\d+(\.\d*)?)|(\.\d+))([eE][\+\-]?\d+)?$'
        return re.fullmatch(number_pattern, s) is not None