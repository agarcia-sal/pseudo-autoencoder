class Solution:
    def reverseWords(self, s: list) -> None:
        # Reverse the entire list to reverse the order of words
        s.reverse()

        start = 0
        for end in range(len(s)):
            if s[end] == ' ':
                # Reverse each individual word to correct their letter order
                s[start:end] = s[start:end][::-1]
                start = end + 1
        # Reverse the last word
        s[start:] = s[start:][::-1]