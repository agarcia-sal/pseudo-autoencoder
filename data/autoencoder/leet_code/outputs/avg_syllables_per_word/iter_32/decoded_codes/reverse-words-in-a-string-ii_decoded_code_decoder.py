from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Reverses the order of words in the list s in-place.
        Each word is reversed individually after the entire list is reversed,
        so that the characters in each word end up in correct order.
        """
        def reverse_sublist(lst: List[str], left: int, right: int) -> None:
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        # Reverse entire list
        reverse_sublist(s, 0, len(s) - 1)

        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                reverse_sublist(s, start, end - 1)
                start = end + 1
        # Reverse the last word
        reverse_sublist(s, start, len(s) - 1)