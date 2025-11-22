from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        def get_canonical_form(s):
            if not s:
                return ""
            canonical_form = []
            first_ord = ord(s[0])
            for c in s:
                diff = (ord(c) - first_ord) % 26
                canonical_form.append(str(diff))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            canonical_form = get_canonical_form(s)
            groups[canonical_form].append(s)

        return list(groups.values())