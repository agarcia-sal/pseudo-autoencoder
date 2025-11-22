from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        # Reverse entire list to invert the order of all elements (words and spaces)
        s.reverse()

        start = 0
        n = len(s)
        for end in range(n):
            if s[end] == ' ':
                # Reverse the word substring from start to end-1
                self._reverse_sublist(s, start, end - 1)
                start = end + 1

        # Reverse the last word after the final space (or the entire string if no space)
        self._reverse_sublist(s, start, n - 1)

    def _reverse_sublist(self, s: List[str], left: int, right: int) -> None:
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1