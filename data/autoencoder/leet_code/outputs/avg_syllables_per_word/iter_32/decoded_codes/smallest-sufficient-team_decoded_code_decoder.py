from typing import List, Dict

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_to_index: Dict[str, int] = {}
        for i, s in enumerate(req_skills):
            skill_to_index[s] = i

        m = len(req_skills)
        n = len(people)

        skill_bits_list = [0] * n
        for i, ss in enumerate(people):
            bits = 0
            for s in ss:
                # Only consider skills that are required
                if s in skill_to_index:
                    bits |= 1 << skill_to_index[s]
            skill_bits_list[i] = bits

        maximum_mask = 1 << m

        # f[mask]: minimum number of people to cover skills represented by mask
        f = [float('inf')] * maximum_mask
        # g[mask]: the last person added to reach the mask with minimal team size
        g = [0] * maximum_mask
        # h[mask]: previous mask before adding the last person
        h = [0] * maximum_mask

        f[0] = 0

        for i in range(maximum_mask):
            if f[i] == float('inf'):
                continue
            for j in range(n):
                new_mask = i | skill_bits_list[j]
                if f[i] + 1 < f[new_mask]:
                    f[new_mask] = f[i] + 1
                    g[new_mask] = j
                    h[new_mask] = i

        i = maximum_mask - 1
        ans = []
        while i != 0:
            ans.append(g[i])
            i = h[i]
        ans.reverse()

        return ans