from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(i: int, j: int, k: int) -> int:
            point_a = trees[i]
            point_b = trees[j]
            point_c = trees[k]
            return (point_b[0] - point_a[0]) * (point_c[1] - point_b[1]) - (point_b[1] - point_a[1]) * (point_c[0] - point_b[0])

        n = len(trees)
        if n < 4:
            return trees

        trees.sort()
        vis = [False] * n
        stk = [0]

        for i in range(1, n):
            while len(stk) > 1 and cross(stk[-2], stk[-1], i) < 0:
                vis[stk.pop()] = False
            vis[i] = True
            stk.append(i)

        m = len(stk)

        for i in range(n - 2, -1, -1):
            if vis[i]:
                continue
            while len(stk) > m and cross(stk[-2], stk[-1], i) < 0:
                stk.pop()
            stk.append(i)

        stk.pop()

        return [trees[i] for i in stk]