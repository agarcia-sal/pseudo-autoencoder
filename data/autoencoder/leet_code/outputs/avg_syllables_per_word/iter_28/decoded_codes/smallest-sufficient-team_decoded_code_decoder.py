from math import inf
from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_to_index = {skill: idx for idx, skill in enumerate(req_skills)}

        total_skills = len(req_skills)
        total_people = len(people)

        skill_bitmasks = [0] * total_people
        for i, p_skills in enumerate(people):
            bitmask = 0
            for skill in p_skills:
                if skill in skill_to_index:
                    bitmask |= 1 << skill_to_index[skill]
            skill_bitmasks[i] = bitmask

        max_state = 1 << total_skills

        f = [inf] * max_state
        g = [-1] * max_state
        h = [-1] * max_state
        f[0] = 0

        for i in range(max_state):
            if f[i] == inf:
                continue
            for j in range(total_people):
                combined_state = i | skill_bitmasks[j]
                if f[i] + 1 < f[combined_state]:
                    f[combined_state] = f[i] + 1
                    g[combined_state] = j
                    h[combined_state] = i

        i = max_state - 1
        answer = []
        while i != 0:
            person = g[i]
            if person == -1:
                break
            answer.append(person)
            i = h[i]

        answer.reverse()
        return answer