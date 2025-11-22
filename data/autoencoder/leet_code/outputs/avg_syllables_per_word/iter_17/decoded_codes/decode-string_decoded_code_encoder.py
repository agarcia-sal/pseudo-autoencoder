class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        a = ""
        d = ""
        for c in s:
            if c.isdigit():
                d += c
            elif c.isalpha():
                a += c
            elif c == '[':
                stack.append((a, int(d)))
                a, d = "", ""
            elif c == ']':
                p, n = stack.pop()
                a = p + a * n
        return a