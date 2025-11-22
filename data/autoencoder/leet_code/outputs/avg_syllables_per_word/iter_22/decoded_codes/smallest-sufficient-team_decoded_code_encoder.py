from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        d = {}
        index_counter = 0
        for s in req_skills:
            d[s] = index_counter
            index_counter += 1
        m = len(req_skills)
        n = len(people)
        p = [0] * n
        for i, ss in enumerate(people):
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
                combined_index = i | p[j]
                if f[i] + 1 < f[combined_index]:
                    f[combined_index] = f[i] + 1
                    g[combined_index] = j
                    h[combined_index] = i
        i = (1 << m) - 1
        ans = []
        while i != 0:
            ans.append(g[i])
            i = h[i]
        return ans