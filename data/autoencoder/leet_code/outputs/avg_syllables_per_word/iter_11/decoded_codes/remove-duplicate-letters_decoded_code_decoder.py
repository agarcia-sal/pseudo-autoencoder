class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}
        for index in range(len(s)):
            character = s[index]
            last_occurrence[character] = index

        stack = []
        in_stack = set()

        for index in range(len(s)):
            character = s[index]
            if character in in_stack:
                continue

            while stack and character < stack[-1] and index < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)

            stack.append(character)
            in_stack.add(character)

        result = ''.join(stack)
        return result