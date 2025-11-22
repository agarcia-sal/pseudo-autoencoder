import re

class Solution:
    def isNumber(self, s: str) -> bool:
        number_regular_expression = r'^[+-]?((\d+(\.\d*)?)|(\.\d+))([eE][+-]?\d+)?$'
        return re.fullmatch(number_regular_expression, s) is not None