from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
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

        size = 1 << m
        f = [float('inf')] * size
        g = [0] * size
        h = [0] * size
        f[0] = 0

        for i in range(size):
            if f[i] == float('inf'):
                continue
            for j in range(n):
                comb = i | p[j]
                if f[i] + 1 < f[comb]:
                    f[comb] = f[i] + 1
                    g[comb] = j
                    h[comb] = i

        i = size - 1
        ans = []
        while i != 0:
            ans.append(g[i])
            i = h[i]
        return ans