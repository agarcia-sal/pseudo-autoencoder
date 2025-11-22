from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(i: int, j: int, k: int) -> int:
            pointA, pointB, pointC = trees[i], trees[j], trees[k]
            dx1 = pointB[0] - pointA[0]
            dy1 = pointB[1] - pointA[1]
            dx2 = pointC[0] - pointB[0]
            dy2 = pointC[1] - pointB[1]
            return dx1 * dy2 - dy1 * dx2

        n = len(trees)
        if n < 4:
            return trees[:]

        trees.sort()
        visited = [False] * n
        stack = [0]

        for i in range(1, n):
            while len(stack) > 1 and cross(stack[-2], stack[-1], i) < 0:
                popped = stack.pop()
                visited[popped] = False
            visited[i] = True
            stack.append(i)

        m = len(stack)

        for i in range(n - 2, -1, -1):
            if visited[i]:
                continue
            while len(stack) > m and cross(stack[-2], stack[-1], i) < 0:
                stack.pop()
            stack.append(i)

        stack.pop()
        return [trees[i] for i in stack]