from collections import deque
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        indeg = [m] * (n - m + 1)
        g = [[] for _ in range(n)]
        q = deque()

        for i in range(n - m + 1):
            for j, c in enumerate(stamp):
                if target[i + j] == c:
                    indeg[i] -= 1
            if indeg[i] == 0:
                q.append(i)
            else:
                for j, c in enumerate(stamp):
                    if target[i + j] != c:
                        g[i + j].append(i)

        ans = []
        vis = [False] * n

        while q:
            i = q.popleft()
            ans.append(i)
            for j in range(m):
                pos = i + j
                if not vis[pos]:
                    vis[pos] = True
                    for k in g[pos]:
                        indeg[k] -= 1
                        if indeg[k] == 0:
                            q.append(k)

        return ans[::-1] if all(vis) else []