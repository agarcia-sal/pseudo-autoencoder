from collections import defaultdict

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_length = defaultdict(int)  # maps character to max length of valid substring ending with that character
        current_length = 0

        for i in range(len(s)):
            if i > 0 and (
                (ord(s[i]) - ord(s[i-1]) == 1) or 
                (s[i] == 'a' and s[i-1] == 'z')
            ):
                current_length += 1
            else:
                current_length = 1

            if current_length > max_length[s[i]]:
                max_length[s[i]] = current_length

        return sum(max_length.values())