from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        def get_canonical_form(s):
            if not s:
                return ""
            canonical_form = []
            first_character = s[0]
            for c in s:
                difference = ord(c) - ord(first_character)
                if difference < 0:
                    difference += 26
                canonical_form.append(str(difference))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            canonical_form = get_canonical_form(s)
            groups[canonical_form].append(s)
        return list(groups.values())