from collections import deque

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
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
                    g[i + j].append(i)

        ans = []
        vis = [False] * n

        while q:
            i = q.popleft()
            ans.append(i)
            for j in range(m):
                idx = i + j
                if not vis[idx]:
                    vis[idx] = True
                    for k in g[idx]:
                        indeg[k] -= 1
                        if indeg[k] == 0:
                            q.append(k)

        if all(vis):
            return ans[::-1]
        return []