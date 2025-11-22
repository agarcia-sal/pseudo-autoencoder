class Solution:
    def smallestSubsequence(self, input_string: str, k: int, letter: str, repetition: int) -> str:
        letter_count = input_string.count(letter)
        stack = []
        for index, char in enumerate(input_string):
            while stack and char < stack[-1] and (len(input_string) - index + len(stack) - 1) >= k:
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
        while len(stack) < k:
            stack.append(letter)
        return ''.join(stack)