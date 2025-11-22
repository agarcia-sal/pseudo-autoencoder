from math import inf
from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        d = {s: i for i, s in enumerate(req_skills)}
        m = len(req_skills)
        n = len(people)

        p = [0] * n
        for i, ss in enumerate(people):
            for s in ss:
                if s in d:
                    p[i] |= 1 << d[s]

        size = 1 << m
        f = [inf] * size
        g = [0] * size
        h = [0] * size
        f[0] = 0

        for i in range(size):
            if f[i] == inf:
                continue
            for j in range(n):
                nxt = i | p[j]
                if f[i] + 1 < f[nxt]:
                    f[nxt] = f[i] + 1
                    g[nxt] = j
                    h[nxt] = i

        ans = []
        i = size - 1
        while i:
            ans.append(g[i])
            i = h[i]
        return ans[::-1]