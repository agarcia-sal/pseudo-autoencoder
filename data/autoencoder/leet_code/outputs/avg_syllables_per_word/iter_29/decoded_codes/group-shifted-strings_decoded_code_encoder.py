from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        def get_canonical_form(s):
            if not s:
                return ""
            canonical_form = []
            first_character_code = ord(s[0]) - ord('a')
            for c in s:
                character_code = ord(c) - ord('a')
                difference = character_code - first_character_code
                if difference < 0:
                    difference += 26
                canonical_form.append(str(difference))
            return ",".join(canonical_form)

        groups = defaultdict(list)
        for s in strings:
            canonical_form = get_canonical_form(s)
            groups[canonical_form].append(s)
        return list(groups.values())