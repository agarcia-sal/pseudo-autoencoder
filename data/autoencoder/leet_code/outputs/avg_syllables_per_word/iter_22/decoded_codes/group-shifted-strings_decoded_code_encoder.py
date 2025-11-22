from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_canonical_form(s: str) -> str:
            if len(s) == 0:
                return ""
            canonical_form = []
            first_ord = ord(s[0])
            for c in s:
                difference = ord(c) - first_ord
                wrapped_difference = difference % 26
                canonical_form.append(str(wrapped_difference))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            canonical_form = get_canonical_form(s)
            groups[canonical_form].append(s)
        return list(groups.values())