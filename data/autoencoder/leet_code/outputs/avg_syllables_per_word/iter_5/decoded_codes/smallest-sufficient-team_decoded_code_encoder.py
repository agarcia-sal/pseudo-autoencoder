class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        m = len(req_skills)
        n = len(people)
        p = [0] * n
        for i, person_skills in enumerate(people):
            mask = 0
            for skill in person_skills:
                if skill in skill_index:
                    mask |= 1 << skill_index[skill]
            p[i] = mask

        size = 1 << m
        f = [float('inf')] * size
        g = [0] * size
        h = [0] * size
        f[0] = 0

        for i in range(size):
            if f[i] == float('inf'):
                continue
            for j in range(n):
                combined = i | p[j]
                if f[i] + 1 < f[combined]:
                    f[combined] = f[i] + 1
                    g[combined] = j
                    h[combined] = i

        ans = []
        i = size - 1
        while i:
            ans.append(g[i])
            i = h[i]
        return ans[::-1]