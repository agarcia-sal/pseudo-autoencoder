class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        a = []
        d = []

        for char in s:
            if char.isdigit():
                d.append(char)
            elif char.isalpha():
                a.append(char)
            elif char == '[':
                stack.append((''.join(a), int(''.join(d)) if d else 0))
                a = []
                d = []
            elif char == ']':
                p, n = stack.pop()
                a = [p + ''.join(a) * n]

        return ''.join(a)