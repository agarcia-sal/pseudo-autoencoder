class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: i for i, char in enumerate(s)}
        stack = []
        in_stack = set()

        for i, char in enumerate(s):
            if char in in_stack:
                continue
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)
            stack.append(char)
            in_stack.add(char)

        return ''.join(stack)