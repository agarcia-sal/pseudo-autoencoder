class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        a = ''
        d = ''
        for ch in s:
            if ch.isdigit():
                d += ch
            elif ch.isalpha():
                a += ch
            elif ch == '[':
                stack.append((a, int(d)))
                a = ''
                d = ''
            elif ch == ']':
                p, n = stack.pop()
                a = p + a * n
        return a