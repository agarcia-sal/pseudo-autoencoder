class Solution:
    def reverseWords(self, s):
        s.reverse()
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                self._reverse(s, start, end - 1)
                start = end + 1
        self._reverse(s, start, len(s) - 1)

    def _reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1