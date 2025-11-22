class Solution:
    def orderlyQueue(self, string_s: str, integer_k: int) -> str:
        if integer_k > 1:
            return self.sortStringDirectly(string_s)
        elif integer_k == 1:
            n = len(string_s)
            smallest = string_s
            for i in range(1, n):
                rotated = string_s[i:] + string_s[:i]
                if rotated < smallest:
                    smallest = rotated
            return smallest

    def sortStringDirectly(self, parameter_string: str) -> str:
        return ''.join(sorted(parameter_string))