import re

def isNumber(s):
    pattern = r'^[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$'
    return re.fullmatch(pattern, s) is not None