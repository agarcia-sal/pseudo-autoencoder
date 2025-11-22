import re
from typing import Pattern


class Solution:
    def isNumber(self, s: str) -> bool:
        number_regex: Pattern = re.compile(
            r'^[\+\-]?(\d+(\.\d*)?|\.\d+)([eE][\+\-]?\d+)?$'
        )
        return bool(number_regex.fullmatch(s.strip()))