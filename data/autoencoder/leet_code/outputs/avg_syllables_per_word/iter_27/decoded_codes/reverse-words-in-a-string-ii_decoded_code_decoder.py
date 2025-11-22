from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        def reverse(lst: List[str], left: int, right: int) -> None:
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        reverse(s, 0, len(s) - 1)
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                reverse(s, start, end - 1)
                start = end + 1
        reverse(s, start, len(s) - 1)