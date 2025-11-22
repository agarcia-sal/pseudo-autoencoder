from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        d = {skill: i for i, skill in enumerate(req_skills)}
        m = len(req_skills)
        n = len(people)
        p = [0] * n
        for i, ss in enumerate(people):
            bitmask = 0
            for s in ss:
                if s in d:
                    bitmask |= 1 << d[s]
            p[i] = bitmask

        f = [inf] * (1 << m)
        g = [0] * (1 << m)
        h = [0] * (1 << m)
        f[0] = 0

        for i in range(1 << m):
            if f[i] == inf:
                continue
            for j in range(n):
                nxt = i | p[j]
                if f[i] + 1 < f[nxt]:
                    f[nxt] = f[i] + 1
                    g[nxt] = j
                    h[nxt] = i

        i = (1 << m) - 1
        ans = []
        while i:
            ans.append(g[i])
            i = h[i]

        return ans