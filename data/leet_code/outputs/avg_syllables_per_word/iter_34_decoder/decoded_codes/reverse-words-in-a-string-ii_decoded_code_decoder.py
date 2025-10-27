class Solution:
    def reverseWords(self, s: list) -> None:
        # reverse entire list
        s.reverse()
        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                # reverse each word back to correct order
                s[start:end] = reversed(s[start:end])
                start = end + 1
        # reverse last word
        s[start:len(s)] = reversed(s[start:len(s)])