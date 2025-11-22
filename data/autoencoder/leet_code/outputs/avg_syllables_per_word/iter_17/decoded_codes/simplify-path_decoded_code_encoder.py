class Solution:
    def simplifyPath(self, path: str) -> str:
        components = self.split_path(path)
        stack = self.initialize_empty_list()
        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if len(stack) > 0:
                    self.remove_last_element(stack)
            else:
                self.append_component(stack, component)
        simplified_path = self.join_stack_with_slashes(stack)
        return simplified_path

    def split_path(self, path: str):
        # splitting path by '/' to get components
        return path.split('/')

    def initialize_empty_list(self):
        return []

    def remove_last_element(self, stack):
        stack.pop()

    def append_component(self, stack, component):
        stack.append(component)

    def join_stack_with_slashes(self, stack):
        # join components with '/' and prepend root '/'
        return '/' + '/'.join(stack)