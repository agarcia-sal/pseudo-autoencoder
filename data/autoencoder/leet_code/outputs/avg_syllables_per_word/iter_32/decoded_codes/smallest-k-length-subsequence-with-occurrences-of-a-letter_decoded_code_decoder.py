from typing import List

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        letter_count = s.count(letter)
        stack: List[str] = []

        for index, char in enumerate(s):
            # Remove chars from the stack if possible to get a lex smaller subsequence
            while stack and char < stack[-1] and (len(s) - index + len(stack) - 1) >= k:
                if stack[-1] == letter:
                    # Only pop if we can still meet repetition requirement later
                    if letter_count > repetition:
                        repetition += 1
                        stack.pop()
                    else:
                        break
                else:
                    stack.pop()

            # Add current char if stack size less than k
            if len(stack) < k:
                if char == letter:
                    stack.append(char)
                    repetition -= 1
                else:
                    # Append if remaining slots after current char are enough to fulfill repetition
                    if k - len(stack) > repetition:
                        stack.append(char)

            # Decrement letter_count if current char is letter as it's processed now
            if char == letter:
                letter_count -= 1

        # If stack is still smaller than k, append letter to fill up to k
        while len(stack) < k:
            stack.append(letter)

        return ''.join(stack)