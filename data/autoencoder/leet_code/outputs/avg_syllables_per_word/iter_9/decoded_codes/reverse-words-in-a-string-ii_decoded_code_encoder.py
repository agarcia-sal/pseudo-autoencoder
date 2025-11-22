class Solution:
    def reverseWords(self, s: list) -> None:
        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        reverse(s, 0, len(s) - 1)
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                reverse(s, start, end - 1)
                start = end + 1
        reverse(s, start, len(s) - 1)