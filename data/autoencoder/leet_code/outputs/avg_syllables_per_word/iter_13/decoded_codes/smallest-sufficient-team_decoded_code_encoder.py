from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        d = {skill: i for i, skill in enumerate(req_skills)}
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
                new_mask = i | p[j]
                if f[i] + 1 < f[new_mask]:
                    f[new_mask] = f[i] + 1
                    g[new_mask] = j
                    h[new_mask] = i
        i = size - 1
        ans = []
        while i:
            ans.append(g[i])
            i = h[i]
        return ans