class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        stack = []
        max_length = 0

        for line in lines:
            depth = line.count('\t')
            name = line[depth:]

            while len(stack) > depth:
                stack.pop()

            if stack:
                current_length = stack[-1] + len(name) + 1  # +1 for '/'
            else:
                current_length = len(name)

            if '.' in name:
                max_length = max(max_length, current_length)
            else:
                stack.append(current_length)

        return max_length