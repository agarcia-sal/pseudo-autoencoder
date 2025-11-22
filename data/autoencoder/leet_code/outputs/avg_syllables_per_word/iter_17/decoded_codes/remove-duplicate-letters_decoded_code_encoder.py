class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Compute the last occurrence of each character in s
        last_occurrence = {}
        for i, ch in enumerate(s):
            last_occurrence[ch] = i

        stack = []
        in_stack = set()

        for i, ch in enumerate(s):
            if ch in in_stack:
                continue
            while stack and ch < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)
            stack.append(ch)
            in_stack.add(ch)

        return ''.join(stack)