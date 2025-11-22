from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s.reverse()
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                self.reverse_sublist(s, start, end - 1)
                start = end + 1
        self.reverse_sublist(s, start, len(s) - 1)

    def reverse_sublist(self, s: List[str], start: int, end: int) -> None:
        left, right = start, end
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1