class Solution:
    def lastSubstring(self, s: str) -> str:
        max_char = max(s)
        candidates = [i for i, ch in enumerate(s) if ch == max_char]
        max_substring = ""
        for start in candidates:
            curr = s[start:]
            if curr > max_substring:
                max_substring = curr
        return max_substring