class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        letter_count = s.count(letter)
        stack = []
        remaining_repetition = repetition

        for i, char in enumerate(s):
            while (stack and char < stack[-1] and 
                   len(s) - i + len(stack) - 1 >= k):
                if stack[-1] == letter:
                    if letter_count > remaining_repetition:
                        remaining_repetition += 1
                        stack.pop()
                    else:
                        break
                else:
                    stack.pop()
            if len(stack) < k:
                if char == letter:
                    stack.append(char)
                    remaining_repetition -= 1
                elif k - len(stack) > remaining_repetition:
                    stack.append(char)
                # If char == letter, letter_count is decremented after insertion
            if char == letter:
                letter_count -= 1

        while len(stack) < k:
            stack.append(letter)

        return ''.join(stack)