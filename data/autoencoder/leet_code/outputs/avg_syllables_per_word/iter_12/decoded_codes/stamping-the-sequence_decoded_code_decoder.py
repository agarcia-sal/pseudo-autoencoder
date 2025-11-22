from collections import deque
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        indeg = [m] * (n - m + 1)
        g = [[] for _ in range(n)]
        q = deque()

        # Build the graph and indegree list
        for i in range(n - m + 1):
            for j, c in enumerate(stamp):
                if target[i + j] == c:
                    indeg[i] -= 1
                else:
                    g[i + j].append(i)
            if indeg[i] == 0:
                q.append(i)

        ans = []
        vis = [False] * n

        # BFS removal of stamps
        while q:
            i = q.popleft()
            ans.append(i)
            for j in range(m):
                if not vis[i + j]:
                    vis[i + j] = True
                    for k in g[i + j]:
                        indeg[k] -= 1
                        if indeg[k] == 0:
                            q.append(k)

        if all(vis):
            return ans[::-1]
        return []