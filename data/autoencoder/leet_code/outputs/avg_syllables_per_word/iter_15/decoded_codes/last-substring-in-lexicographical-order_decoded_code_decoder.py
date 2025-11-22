from typing import List

class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        max_char = max(s)
        max_indices: List[int] = []
        for index in range(n):
            if s[index] == max_char:
                max_indices.append(index)

        max_substring = ""
        for start in max_indices:
            current_substring = s[start:]
            if current_substring > max_substring:
                max_substring = current_substring

        return max_substring