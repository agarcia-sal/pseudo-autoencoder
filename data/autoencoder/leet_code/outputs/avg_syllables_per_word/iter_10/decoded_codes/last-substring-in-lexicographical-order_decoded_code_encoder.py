class Solution:
    def lastSubstring(self, s: str) -> str:
        max_char = max(s)
        max_substring = ""
        for i, ch in enumerate(s):
            if ch == max_char:
                candidate = s[i:]
                if candidate > max_substring:
                    max_substring = candidate
        return max_substring