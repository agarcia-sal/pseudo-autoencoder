class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        a = ''
        d = ''
        for character in s:
            if character.isdigit():
                d += character
            elif character.isalpha():
                a += character
            elif character == '[':
                stack.append((a, int(d)))
                a = ''
                d = ''
            elif character == ']':
                p, n = stack.pop()
                a = p + a * n
        return a