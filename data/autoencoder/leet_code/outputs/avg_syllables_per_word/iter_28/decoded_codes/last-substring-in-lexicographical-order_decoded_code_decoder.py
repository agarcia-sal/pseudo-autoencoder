from typing import List

class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        max_char = max(s)
        max_indices: List[int] = [i for i, ch in enumerate(s) if ch == max_char]

        max_substring = ""
        for start in max_indices:
            current_substring = s[start:]
            if current_substring > max_substring:
                max_substring = current_substring
        return max_substring