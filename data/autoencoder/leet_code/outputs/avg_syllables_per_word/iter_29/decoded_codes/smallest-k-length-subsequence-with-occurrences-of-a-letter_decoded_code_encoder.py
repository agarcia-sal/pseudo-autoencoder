class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        letter_count = s.count(letter)
        stack = []
        index = 0
        n = len(s)

        for character in s:
            while stack and character < stack[-1] and (n - index + len(stack) - 1) >= k:
                if stack[-1] == letter:
                    if letter_count > repetition:
                        repetition += 1
                        stack.pop()
                    else:
                        break
                else:
                    stack.pop()
            if len(stack) < k:
                if character == letter:
                    stack.append(character)
                    repetition -= 1
                elif k - len(stack) > repetition:
                    stack.append(character)
            if character == letter:
                letter_count -= 1
            index += 1

        while len(stack) < k:
            stack.append(letter)

        return ''.join(stack)