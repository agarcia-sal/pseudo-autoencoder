class Solution:
    def reverseWords(self, s: list) -> None:
        # Reverse the entire list
        s.reverse()
        start = 0
        n = len(s)
        for end in range(n):
            if s[end] == ' ':
                # Reverse the word from start to end-1
                left, right = start, end - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                start = end + 1
        # Reverse the last word
        left, right = start, n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1