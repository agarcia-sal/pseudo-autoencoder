from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        def get_canonical_form(s):
            if not s:
                return ""
            base = ord(s[0])
            return ",".join(str((ord(c) - base) % 26) for c in s)

        groups = defaultdict(list)
        for s in strings:
            groups[get_canonical_form(s)].append(s)

        return list(groups.values())