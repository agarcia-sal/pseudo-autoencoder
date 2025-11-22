from typing import Dict, Set, List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence: Dict[str, int] = {}
        for i, c in enumerate(s):
            last_occurrence[c] = i

        stack: List[str] = []
        in_stack: Set[str] = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                removed_char = stack.pop()
                in_stack.remove(removed_char)
            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)