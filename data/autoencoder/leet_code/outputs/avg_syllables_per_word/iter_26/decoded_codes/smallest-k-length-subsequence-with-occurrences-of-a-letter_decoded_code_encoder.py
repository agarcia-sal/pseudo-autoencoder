class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        letter_count = s.count(letter)
        stack = []

        for i, char in enumerate(s):
            while stack and char < stack[-1] and (len(s) - i + len(stack) - 1) >= k:
                if stack[-1] == letter:
                    if letter_count > repetition:
                        repetition += 1
                        stack.pop()
                    else:
                        break
                else:
                    stack.pop()

            if len(stack) < k:
                if char == letter:
                    stack.append(char)
                    repetition -= 1
                elif k - len(stack) > repetition:
                    stack.append(char)

                if char == letter:
                    letter_count -= 1
            else:
                if char == letter:
                    letter_count -= 1

        while len(stack) < k:
            stack.append(letter)

        return ''.join(stack)