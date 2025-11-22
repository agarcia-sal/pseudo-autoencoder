from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        def get_canonical_form(s):
            if s == "":
                return ""
            base = ord(s[0])
            canonical_form = []
            for c in s:
                offset = (ord(c) - base) % 26
                canonical_form.append(str(offset))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            key = get_canonical_form(s)
            groups[key].append(s)
        return list(groups.values())