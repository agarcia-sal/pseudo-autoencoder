from typing import List

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines: List[str] = input.split('\n')
        stack: List[int] = []
        max_length: int = 0

        for line in lines:
            depth = line.count('\t')
            name = line[depth:]

            while len(stack) > depth:
                stack.pop()

            if stack:
                current_length = stack[-1] + len(name) + 1
            else:
                current_length = len(name)

            if '.' in name:
                max_length = max(max_length, current_length)
            else:
                stack.append(current_length)

        return max_length