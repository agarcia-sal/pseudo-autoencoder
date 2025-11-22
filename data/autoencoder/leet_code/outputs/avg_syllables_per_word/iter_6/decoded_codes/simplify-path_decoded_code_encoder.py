class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []
        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        return '/' + '/'.join(stack)