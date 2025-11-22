from collections import defaultdict
from typing import List, Dict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_canonical_form(s: str) -> str:
            if s == "":
                return ""
            base_ord = ord(s[0])
            canonical_form = []
            for c in s:
                # Calculate circular difference in alphabet with wrap-around using modulo 26
                diff = (ord(c) - base_ord) % 26
                canonical_form.append(str(diff))
            return ",".join(canonical_form)

        groups: Dict[str, List[str]] = defaultdict(list)
        for s in strings:
            canonical_form = get_canonical_form(s)
            groups[canonical_form].append(s)
        return list(groups.values())