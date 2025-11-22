class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue

            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)

            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)