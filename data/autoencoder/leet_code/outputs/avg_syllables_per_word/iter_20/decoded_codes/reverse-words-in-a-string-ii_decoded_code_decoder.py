class Solution:
    def reverseWords(self, s: list[str]) -> None:
        s.reverse()
        start = 0
        n = len(s)
        for end in range(n):
            if s[end] == ' ':
                s[start:end] = s[start:end][::-1]
                start = end + 1
        s[start:n] = s[start:n][::-1]