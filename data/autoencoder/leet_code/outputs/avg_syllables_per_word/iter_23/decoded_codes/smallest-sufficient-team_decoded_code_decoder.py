from typing import List
import math

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Map each skill to an index
        d = {}
        i = 0
        for s in req_skills:
            d[s] = i
            i += 1
        m = len(req_skills)
        n = len(people)

        # Represent each person's skills as a bitmask
        p = [0] * n
        for i, ss in enumerate(people):
            for s in ss:
                if s in d:
                    p[i] |= 1 << d[s]

        # f[state] = minimum number of people to cover skills represented by state bitmask
        f = [math.inf] * (1 << m)
        # g[state] = index of last person added to achieve state
        g = [0] * (1 << m)
        # h[state] = previous state before last person added
        h = [0] * (1 << m)
        f[0] = 0

        for i in range(1 << m):
            if f[i] == math.inf:
                continue
            for j in range(n):
                new_state = i | p[j]
                if f[i] + 1 < f[new_state]:
                    f[new_state] = f[i] + 1
                    g[new_state] = j
                    h[new_state] = i

        i = (1 << m) - 1
        ans = []
        while i != 0:
            ans.append(g[i])
            i = h[i]
        ans.reverse()
        return ans