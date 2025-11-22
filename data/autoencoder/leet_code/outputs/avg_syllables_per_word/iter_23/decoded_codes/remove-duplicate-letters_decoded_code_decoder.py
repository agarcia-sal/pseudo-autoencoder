class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}
        for index, character in enumerate(s):
            last_occurrence[character] = index

        stack = []
        in_stack = set()

        for index, character in enumerate(s):
            if character in in_stack:
                continue

            while stack and character < stack[-1] and index < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)

            stack.append(character)
            in_stack.add(character)

        result_string = ''.join(stack)
        return result_string