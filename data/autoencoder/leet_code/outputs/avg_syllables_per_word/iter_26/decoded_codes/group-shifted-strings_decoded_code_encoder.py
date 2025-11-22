from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        def get_canonical_form(s):
            if s == "":
                return ""
            canonical_form = []
            base = ord(s[0])
            for c in s:
                difference = ord(c) - base
                wrapped_difference = difference % 26
                canonical_form.append(str(wrapped_difference))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            canonical_form = get_canonical_form(s)
            groups[canonical_form].append(s)
        return list(groups.values())