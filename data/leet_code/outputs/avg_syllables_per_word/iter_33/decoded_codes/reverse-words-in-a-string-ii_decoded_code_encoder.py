class Solution:
    def reverseWords(self, s: list) -> None:
        # Reverse the entire list in place
        s.reverse()
        start = 0
        n = len(s)
        for end in range(n):
            if s[end] == ' ':
                # Reverse the current word in place
                s[start:end] = s[start:end][::-1]
                start = end + 1
        # Reverse the last word
        s[start:n] = s[start:n][::-1]