from collections import defaultdict

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # max_length[c] will store the max length of a valid substring ending with character c
        max_length = defaultdict(int)
        current_length = 0

        for i in range(len(s)):
            if i > 0 and ((ord(s[i]) - ord(s[i - 1]) == 1) or (s[i - 1] == 'z' and s[i] == 'a')):
                current_length += 1
            else:
                current_length = 1
            max_length[s[i]] = max(max_length[s[i]], current_length)

        return sum(max_length.values())