from typing import Dict

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_length: Dict[str, int] = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        current_length = 0
        for i in range(len(s)):
            if (
                i > 0 and 
                (ord(s[i]) - ord(s[i - 1]) == 1 or (s[i] == 'a' and s[i - 1] == 'z'))
            ):
                current_length += 1
            else:
                current_length = 1
            max_length[s[i]] = max(max_length[s[i]], current_length)
        return sum(max_length.values())