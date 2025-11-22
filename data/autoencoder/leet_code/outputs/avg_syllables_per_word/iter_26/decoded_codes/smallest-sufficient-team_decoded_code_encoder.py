from typing import List

class Solution:
    def smallestSufficientTeam(self, required_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_to_index = {skill: i for i, skill in enumerate(required_skills)}
        n_skills = len(required_skills)
        n_people = len(people)

        people_skill_mask = [0] * n_people
        for i, skills in enumerate(people):
            mask = 0
            for skill in skills:
                if skill in skill_to_index:
                    mask |= 1 << skill_to_index[skill]
            people_skill_mask[i] = mask

        max_state = 1 << n_skills
        f = [float('inf')] * max_state
        g = [0] * max_state
        h = [0] * max_state
        f[0] = 0

        for state in range(max_state):
            if f[state] == float('inf'):
                continue
            for i in range(n_people):
                new_state = state | people_skill_mask[i]
                if f[state] + 1 < f[new_state]:
                    f[new_state] = f[state] + 1
                    g[new_state] = i
                    h[new_state] = state

        res = []
        curr = max_state - 1
        while curr != 0:
            res.append(g[curr])
            curr = h[curr]

        return res