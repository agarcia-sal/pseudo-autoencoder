from typing import Dict, Set, List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence: Dict[str, int] = {char: idx for idx, char in enumerate(s)}
        stack: List[str] = []
        in_stack: Set[str] = set()

        for idx, char in enumerate(s):
            if char in in_stack:
                continue

            while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)

            stack.append(char)
            in_stack.add(char)

        return ''.join(stack)