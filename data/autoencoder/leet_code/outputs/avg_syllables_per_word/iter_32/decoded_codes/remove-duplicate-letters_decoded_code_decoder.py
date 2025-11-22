from typing import Dict, Set, List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence: Dict[str, int] = {}
        for index, char in enumerate(s):
            last_occurrence[char] = index

        stack: List[str] = []
        in_stack: Set[str] = set()

        for index, char in enumerate(s):
            if char in in_stack:
                continue

            while stack and char < stack[-1] and index < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)

            stack.append(char)
            in_stack.add(char)

        return ''.join(stack)