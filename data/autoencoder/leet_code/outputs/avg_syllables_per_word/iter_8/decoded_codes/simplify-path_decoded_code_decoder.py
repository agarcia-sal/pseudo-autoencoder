class Solution:
    def simplifyPath(self, path):
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
        simplified_path = '/' + '/'.join(stack)
        return simplified_path