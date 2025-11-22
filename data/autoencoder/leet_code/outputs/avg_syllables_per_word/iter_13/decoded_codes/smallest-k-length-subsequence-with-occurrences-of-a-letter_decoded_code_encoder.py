class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        letter_count = s.count(letter)
        stack = []
        for i, c in enumerate(s):
            while stack and c < stack[-1] and len(s) - i + len(stack) - 1 >= k:
                if stack[-1] == letter:
                    if letter_count > repetition:
                        repetition += 1
                        stack.pop()
                    else:
                        break
                else:
                    stack.pop()
            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    repetition -= 1
                elif k - len(stack) > repetition:
                    stack.append(c)
                if c == letter:
                    letter_count -= 1
            else:
                if c == letter:
                    letter_count -= 1
        while len(stack) < k:
            stack.append(letter)
        return ''.join(stack)