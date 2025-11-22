class Solution:
    def lastSubstring(self, s: str) -> str:
        max_char = max(s)
        max_substring = ""
        for i, c in enumerate(s):
            if c == max_char:
                if s[i:] > max_substring:
                    max_substring = s[i:]
        return max_substring