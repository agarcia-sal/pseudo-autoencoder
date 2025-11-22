from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        # Map each skill to a distinct index
        d = {skill: idx for idx, skill in enumerate(req_skills)}
        m = len(req_skills)
        n = len(people)

        # Convert each person's skill list into a bitmask
        p = [0] * n
        for i, skills in enumerate(people):
            for skill in skills:
                if skill in d:
                    p[i] |= 1 << d[skill]

        size = 1 << m
        f = [inf] * size
        g = [0] * size
        h = [0] * size
        f[0] = 0

        for i in range(size):
            if f[i] == inf:
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
        ans.reverse()
        return ans