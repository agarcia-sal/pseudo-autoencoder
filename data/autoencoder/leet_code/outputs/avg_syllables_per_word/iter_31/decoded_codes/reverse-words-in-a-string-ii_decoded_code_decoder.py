from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Reverses the order of words in the list s in-place.
        Words are separated by single space characters.
        """
        def reverse_range(lst: List[str], left: int, right: int) -> None:
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        n = len(s)
        # Reverse the entire list
        reverse_range(s, 0, n - 1)

        start = 0
        for end in range(n):
            if s[end] == ' ':
                reverse_range(s, start, end - 1)
                start = end + 1

        # Reverse the last word
        reverse_range(s, start, n - 1)