from collections import deque
from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        indeg = [m] * (n - m + 1)  # indegree count per window
        g = [[] for _ in range(n)]  # adjacency list for positions
        q = deque()

        for i in range(n - m + 1):
            for j in range(m):
                if target[i + j] == stamp[j]:
                    indeg[i] -= 1
                    if indeg[i] == 0:
                        q.append(i)
                else:
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

        if all(vis):
            return ans[::-1]
        return []