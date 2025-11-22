from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_index_map = {}
        index_counter = 0
        for skill in req_skills:
            skill_index_map[skill] = index_counter
            index_counter += 1

        number_of_skills = len(req_skills)
        number_of_people = len(people)

        skill_mask_list = [0] * number_of_people
        for i, ss in enumerate(people):
            mask = 0
            for s in ss:
                if s in skill_index_map:  # Defensive check
                    mask |= 1 << skill_index_map[s]
            skill_mask_list[i] = mask

        max_state = 1 << number_of_skills
        f = [inf] * max_state
        g = [0] * max_state
        h = [0] * max_state
        f[0] = 0

        for i in range(max_state):
            if f[i] == inf:
                continue
            for j in range(number_of_people):
                new_state = i | skill_mask_list[j]
                if f[i] + 1 < f[new_state]:
                    f[new_state] = f[i] + 1
                    g[new_state] = j
                    h[new_state] = i

        i = max_state - 1
        answer_list = []
        while i != 0:
            answer_list.append(g[i])
            i = h[i]
        answer_list.reverse()
        return answer_list