from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s.reverse()
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                s[start:end] = reversed(s[start:end])
                start = end + 1
        s[start:] = reversed(s[start:])