class Solution:
    def reverseWords(self, s: list) -> None:
        # Reverse the entire list first
        s.reverse()
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                # Reverse the segment of the word
                s[start:end] = s[start:end][::-1]
                start = end + 1
        # Reverse the last word segment
        s[start:] = s[start:][::-1]