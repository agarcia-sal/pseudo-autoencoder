class Solution:
    def reverseWords(self, s: list[str]) -> None:
        # Helper function to reverse a sublist in place from left to right indices inclusive
        def reverse_sublist(lst: list[str], left: int, right: int) -> None:
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        # Reverse the entire list first
        reverse_sublist(s, 0, len(s) - 1)

        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                reverse_sublist(s, start, end - 1)
                start = end + 1

        # Reverse the last word
        reverse_sublist(s, start, len(s) - 1)