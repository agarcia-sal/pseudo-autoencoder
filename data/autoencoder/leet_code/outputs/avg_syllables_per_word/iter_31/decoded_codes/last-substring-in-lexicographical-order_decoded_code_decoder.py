class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        max_char = max(s)
        max_substring = ""
        for index, ch in enumerate(s):
            if ch == max_char:
                current_substring = s[index:]
                if current_substring > max_substring:
                    max_substring = current_substring
        return max_substring