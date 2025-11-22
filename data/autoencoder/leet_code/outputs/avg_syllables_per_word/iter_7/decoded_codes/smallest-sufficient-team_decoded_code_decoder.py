from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        d = {skill: i for i, skill in enumerate(req_skills)}
        m = len(req_skills)
        n = len(people)
        p = [0] * n

        for i, ss in enumerate(people):
            for s in ss:
                p[i] |= 1 << d[s]

        f = [float('inf')] * (1 << m)
        g = [0] * (1 << m)
        h = [0] * (1 << m)
        f[0] = 0

        for i in range(1 << m):
            if f[i] == float('inf'):
                continue
            for j in range(n):
                comb = i | p[j]
                if f[i] + 1 < f[comb]:
                    f[comb] = f[i] + 1
                    g[comb] = j
                    h[comb] = i

        i = (1 << m) - 1
        ans = []
        while i != 0:
            ans.append(g[i])
            i = h[i]

        return ans