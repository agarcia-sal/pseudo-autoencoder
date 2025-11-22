class Solution:
    def reverseWords(self, s: list) -> None:
        # Reverse the entire list
        s.reverse()
        start = 0
        # Iterate over the characters by index
        for end in range(len(s)):
            if s[end] == ' ':
                # Reverse the sublist from start to end-1
                s[start:end] = reversed(s[start:end])
                start = end + 1
        # Reverse the last word after the last space (or the entire string if no space)
        s[start:] = reversed(s[start:])