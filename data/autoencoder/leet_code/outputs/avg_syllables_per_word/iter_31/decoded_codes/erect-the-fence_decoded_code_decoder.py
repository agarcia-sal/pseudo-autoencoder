from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(i: int, j: int, k: int) -> int:
            p1, p2, p3 = trees[i], trees[j], trees[k]
            return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])

        n = len(trees)
        if n < 4:
            return trees[:]

        trees.sort()
        vis = [False] * n
        stk = [0]

        for i in range(1, n):
            while len(stk) > 1 and cross(stk[-2], stk[-1], i) < 0:
                popped_index = stk.pop()
                vis[popped_index] = False
            vis[i] = True
            stk.append(i)

        m = len(stk)
        for i in range(n - 2, -1, -1):
            if vis[i]:
                continue
            while len(stk) > m and cross(stk[-2], stk[-1], i) < 0:
                stk.pop()
            stk.append(i)

        stk.pop()  # remove last to avoid duplication

        result = [trees[i] for i in stk]

        return result