class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        a = ""
        d = ""
        for char in s:
            if char.isdigit():
                d += char
            elif char.isalpha():
                a += char
            elif char == '[':
                stack.append((a, int(d)))
                a = ""
                d = ""
            elif char == ']':
                p, n = stack.pop()
                a = p + a * n
        return a