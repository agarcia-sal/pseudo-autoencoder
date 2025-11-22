from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(i: int, j: int, k: int) -> int:
            point_a = trees[i]
            point_b = trees[j]
            point_c = trees[k]
            return (
                (point_b[0] - point_a[0]) * (point_c[1] - point_b[1])
                - (point_b[1] - point_a[1]) * (point_c[0] - point_b[0])
            )

        n = len(trees)
        if n < 4:
            return trees

        trees.sort()
        visited = [False] * n
        stack = [0]

        for i in range(1, n):
            while len(stack) > 1 and cross(stack[-2], stack[-1], i) < 0:
                removed = stack.pop()
                visited[removed] = False
            visited[i] = True
            stack.append(i)

        m = len(stack)
        for i in range(n - 2, -1, -1):
            if visited[i]:
                continue
            while len(stack) > m and cross(stack[-2], stack[-1], i) < 0:
                stack.pop()
            stack.append(i)

        stack.pop()  # remove the last element to avoid duplication

        return [trees[i] for i in stack]