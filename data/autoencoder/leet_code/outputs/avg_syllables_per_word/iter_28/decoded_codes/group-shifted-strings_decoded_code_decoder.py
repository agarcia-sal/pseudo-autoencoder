from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_canonical_form(s: str) -> str:
            if not s:
                return ""
            base = ord(s[0])
            alphabet_size = 26
            canonical_form = []
            for c in s:
                diff = (ord(c) - base) % alphabet_size
                canonical_form.append(str(diff))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            key = get_canonical_form(s)
            groups[key].append(s)

        return list(groups.values())