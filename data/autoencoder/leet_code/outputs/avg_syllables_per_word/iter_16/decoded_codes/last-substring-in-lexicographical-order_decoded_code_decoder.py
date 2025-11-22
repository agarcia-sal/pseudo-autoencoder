class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        max_char = max(s)
        max_indices = [i for i in range(n) if s[i] == max_char]
        max_substring = ""
        for start in max_indices:
            current_substring = s[start:]
            if current_substring > max_substring:
                max_substring = current_substring
        return max_substring