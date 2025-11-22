from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        d = {s: i for i, s in enumerate(req_skills)}
        m = len(req_skills)
        n = len(people)

        p = [0] * n
        for i, skill_list in enumerate(people):
            bitmask = 0
            for s in skill_list:
                if s in d:
                    bitmask |= 1 << d[s]
            p[i] = bitmask

        size = 1 << m
        INF = float('inf')
        f = [INF] * size
        g = [0] * size  # store last person index
        h = [0] * size  # store previous state
        f[0] = 0

        for i in range(size):
            if f[i] == INF:
                continue
            for j in range(n):
                nxt = i | p[j]
                if f[i] + 1 < f[nxt]:
                    f[nxt] = f[i] + 1
                    g[nxt] = j
                    h[nxt] = i

        i = size - 1
        ans = []
        while i != 0:
            ans.append(g[i])
            i = h[i]

        ans.reverse()
        return ans