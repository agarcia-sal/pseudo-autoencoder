class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        m, n = len(req_skills), len(people)
        p = [0] * n
        for i, skills in enumerate(people):
            bitmask = 0
            for skill in skills:
                if skill in skill_index:
                    bitmask |= 1 << skill_index[skill]
            p[i] = bitmask

        INF = float('inf')
        f = [INF] * (1 << m)
        g = [0] * (1 << m)
        h = [0] * (1 << m)
        f[0] = 0

        for i in range(1 << m):
            if f[i] == INF:
                continue
            for j in range(n):
                combined = i | p[j]
                if f[i] + 1 < f[combined]:
                    f[combined] = f[i] + 1
                    g[combined] = j
                    h[combined] = i

        res = []
        i = (1 << m) - 1
        while i:
            res.append(g[i])
            i = h[i]
        return res[::-1]