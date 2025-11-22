from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_canonical_form(s: str) -> str:
            if s == "":
                return ""
            first_char_code = ord(s[0])
            canonical_form = []
            for c in s:
                diff = (ord(c) - first_char_code) % 26
                canonical_form.append(str(diff))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            canonical_form = get_canonical_form(s)
            groups[canonical_form].append(s)
        return list(groups.values())