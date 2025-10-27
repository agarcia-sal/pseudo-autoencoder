from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        def get_canonical_form(s):
            if s == "":
                return ""
            base = ord(s[0])
            canonical_form = []
            for c in s:
                diff = (ord(c) - base) % 26
                canonical_form.append(str(diff))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            canonical_form = get_canonical_form(s)
            groups[canonical_form].append(s)
        return list(groups.values())