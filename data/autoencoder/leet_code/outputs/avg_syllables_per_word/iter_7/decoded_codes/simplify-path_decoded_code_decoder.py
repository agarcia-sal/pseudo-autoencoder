from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        components: List[str] = path.split('/')
        stack: List[str] = []
        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        simplified_path: str = '/' + '/'.join(stack)
        return simplified_path