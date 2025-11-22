from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        d = {}
        for i in range(len(req_skills)):
            s = req_skills[i]
            d[s] = i

        m = len(req_skills)
        n = len(people)

        p = [0] * n

        for i in range(n):
            ss = people[i]
            for s in ss:
                p[i] |= 1 << d[s]

        f = [inf] * (1 << m)
        g = [0] * (1 << m)
        h = [0] * (1 << m)

        f[0] = 0

        for i in range(1 << m):
            if f[i] == inf:
                continue
            for j in range(n):
                new_mask = i | p[j]
                if f[i] + 1 < f[new_mask]:
                    f[new_mask] = f[i] + 1
                    g[new_mask] = j
                    h[new_mask] = i

        i = (1 << m) - 1
        ans = []
        while i != 0:
            ans.append(g[i])
            i = h[i]

        return ans